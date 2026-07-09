import logging
import os
import time

from framework.pages.share_cubii_page import ShareCubiiPage


class CubiiStorePage(ShareCubiiPage):
    LOGGER = logging.getLogger("cubii_store_page")

    STORE_URL_HOST_FRAGMENT_DEFAULT = "cubii.com"
    STORE_URL_PATH_FRAGMENT_DEFAULT = "products"

    def _store_url_fragment(self) -> str:
        return (
            os.getenv("CUBII_STORE_URL_FRAGMENT")
            or self.STORE_URL_HOST_FRAGMENT_DEFAULT
        ).strip().lower()

    def _store_url_path_fragment(self) -> str:
        return (
            os.getenv("CUBII_STORE_URL_PATH_FRAGMENT")
            or self.STORE_URL_PATH_FRAGMENT_DEFAULT
        ).strip().lower()

    def verify_cubii_store_link_opened(self) -> None:
        """
        Assert The Cubii Store opened the store URL in external Chrome after cookie dismiss.
        Primary check: Chrome foreground + cubii.com/products URL in address bar or WEBVIEW.
        """
        url_fragment = self._store_url_fragment()
        path_fragment = self._store_url_path_fragment()
        self.LOGGER.info(
            "Verifying The Cubii Store link opened in Chrome "
            "(host=%r, path=%r).",
            url_fragment,
            path_fragment,
        )
        package = self._wait_for_chrome_foreground()

        wait_sec = int(os.getenv("CUBII_STORE_VERIFY_URL_WAIT_SEC", "20"))
        pause = float(os.getenv("CUBII_STORE_VERIFY_URL_POLL_SEC", "0.5"))
        deadline = time.time() + wait_sec
        url_text = ""

        while time.time() < deadline:
            url_text = self._read_browser_url_text(url_fragment)
            if not url_text:
                url_text = self._read_url_from_webview_context(url_fragment)
            if url_text and path_fragment in url_text.lower():
                break
            url_text = ""
            time.sleep(pause)

        if not url_text:
            raise AssertionError(
                f"Chrome is open (package={package!r}) but a Cubii Store URL "
                f"({url_fragment!r} + {path_fragment!r}) was not found in the "
                f"address bar or WEBVIEW within {wait_sec}s."
            )

        if self._is_chrome_cookie_overlay_visible():
            raise AssertionError(
                "Chrome shows the Cubii Store URL but the cookie consent overlay "
                "is still visible."
            )

        self.LOGGER.info(
            "Verified The Cubii Store link opened in Chrome (package=%s, url=%r).",
            package,
            url_text,
        )

    def _read_browser_url_text(self, url_fragment: str) -> str:
        for by, locator in self.CHROME_URL_BAR_LOCATORS:
            try:
                for element in self.driver.find_elements(by, locator):
                    if not element.is_displayed():
                        continue
                    text = (
                        (element.text or "")
                        + " "
                        + (element.get_attribute("text") or "")
                    ).strip()
                    if url_fragment in text.lower():
                        return text
            except Exception:
                continue
        return ""

    def _read_url_from_webview_context(self, url_fragment: str) -> str:
        for ctx in self._list_chrome_webview_contexts():
            try:
                self.driver.switch_to.context(ctx)
                url = (getattr(self.driver, "current_url", None) or "") or ""
                if url_fragment in url.lower():
                    self.LOGGER.info(
                        "Found store URL in WEBVIEW context %r: %s", ctx, url
                    )
                    return url
            except Exception as exc:
                self.LOGGER.debug("WEBVIEW URL read failed for %r: %s", ctx, exc)
            finally:
                try:
                    self.driver.switch_to.context("NATIVE_APP")
                except Exception:
                    pass
        return ""
