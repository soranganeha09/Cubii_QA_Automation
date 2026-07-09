# Troubleshooting

Common issues when running Cubii mobile BDD automation (Appium + Behave + ADB).

---

## ADB: daemon fails to start (`Too many open files`)

### Symptoms

```text
adb devices
* daemon not running; starting now at tcp:5037
ADB server didn't ACK
failed to create inotify fd: Too many open files
* failed to start daemon
adb: failed to check server version: cannot connect to daemon
```

After `pkill -9 adb` and `adb kill-server`, you may see:

```text
cannot connect to daemon at tcp:5037: Connection refused
```

That message is **normal** when no ADB server is running.

### What it means

| Message | Meaning |
|--------|---------|
| `ADB server didn't ACK` | The ADB server process started but crashed before it could respond. |
| `failed to create inotify fd: Too many open files` | **Root cause** — Linux refused a new file descriptor (`EMFILE`). ADB’s USB hotplug code needs an `inotify` handle and cannot create one. |
| `* failed to start daemon` | No ADB server is running. |
| `cannot connect to daemon` | The `adb` client has nothing to talk to. |

This is an **environment / OS resource** problem, not a Cubii app or test-code bug. Behave and Appium cannot connect to a device until ADB starts successfully.

### What it is not

- Not caused by a specific `.feature` file or step definition
- Not “phone unplugged” alone — ADB fails before it can list devices
- Not fixed by only re-running tests without freeing resources

### Typical causes

- Many open file descriptors from **Chrome**, **Cursor**, **Appium Inspector**, or leftover **Node / Appium / Java** processes
- Long test sessions without closing Appium Inspector or browsers
- Stuck or repeated `adb start-server` attempts after crashes

### Fix (try in order)

1. **Stop automation and heavy apps**
   - Close Appium Inspector
   - Stop running `behave` / Appium sessions
   - Close extra browser windows if possible

2. **Kill stuck ADB and Appium processes**

   ```bash
   pkill -9 adb
   pkill -f appium
   ```

   `adb kill-server` may print `Connection refused` — that is OK if no daemon was running.

3. **Start ADB again**

   ```bash
   adb start-server
   adb devices
   ```

   You should see your device with status `device` (not `offline` or `unauthorized`).

4. **Check limits (optional)**

   ```bash
   ulimit -n
   cat /proc/sys/fs/file-nr
   tail -20 /tmp/adb.$(id -u).log
   ```

   A high `ulimit -n` does not always prevent this error if the system or `inotify` limits are stressed.

5. **If ADB still fails**
   - Log out and log back in, or **reboot** the machine
   - Reconnect the phone (USB or wireless debugging)
   - Run `adb devices` again

6. **Device shows `offline` or `unauthorized`**

   ```bash
   adb kill-server
   adb start-server
   adb devices
   ```

   On the phone: accept the USB debugging prompt, or re-pair wireless debugging.

### Before running tests

Confirm ADB works **before** starting Appium or Behave:

```bash
adb devices
# Expected: List of devices attached
# <serial>    device
```

If this command fails with `Too many open files`, fix ADB first — no mobile test run will work until it does.

### Log location

ADB startup errors are appended to:

```text
/tmp/adb.<your-user-id>.log
```

Example: `/tmp/adb.1000.log` for UID 1000.

---

## Related: device `offline` after `adb` was working

If `adb devices` worked earlier but the device is now `offline`:

```bash
adb kill-server
adb start-server
adb devices
```

Restart wireless debugging on the phone if you use Wi‑Fi ADB, or reconnect the USB cable.
