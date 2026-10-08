# Sadhya

A pastel, day-wise placement prep tracker for 9 to 30 October 2026. It installs as a real app with its own icon:

- **Android:** an APK that GitHub builds for you automatically.
- **Laptop or any phone:** an installable web app (PWA) that opens in its own window.

Every task comes from the plan's **Sufficient resource** columns. Add-on resources are left out on purpose.

- **Today**: a date strip, then Conceptual and Coding tabs. Coding is split into *DSA / SQL practice* and *ML / DL coding & projects*.
- **Carry-over**: anything not fully ticked on its day moves to the top of today in red until it's done.
- **Plan**: every topic by date, with search and filters (area, track, priority, status).
- **Insights**: overall %, due-so-far %, streak, days left, remaining work vs plan, activity calendar, and date-wise, area-wise, track and priority breakdowns.
- **Settings**: install, theme, back up / restore progress, clear progress.

---

## 1. Put it on GitHub

**Without the command line**

1. Sign in at github.com, click **New repository**, name it `sadhya`, choose **Public**, and create it.
2. On the empty repo page, click **uploading an existing file**.
3. Drag in everything from this folder, including the hidden `.github` folder, and click **Commit changes**.

Your file picker may hide folders that start with a dot, so `.github` often doesn't upload. Check the repo for a `.github` folder. If it's missing:

1. In the repo, click **Add file → Create new file**.
2. Type the name exactly as `.github/workflows/build-apk.yml` (the slashes create the folders).
3. Open `COPY-ME-build-apk.yml` from this folder, copy everything in it, paste it in, and click **Commit changes**.

**Or with git**

```bash
cd sadhya
git init
git add .
git commit -m "Sadhya"
git branch -M main
git remote add origin https://github.com/<your-username>/sadhya.git
git push -u origin main
```

## 2. Get the Android app (APK)

Every push to `main` builds the app automatically.

1. Open the repo's **Actions** tab and wait for **Build Sadhya APK** to turn green. It takes about 5–8 minutes.
2. Open **Releases** on the right side of the repo page and download `Sadhya.apk` from the newest release.
3. On your phone, open the downloaded file. If asked, allow installs from your browser or file manager, then tap **Install**. If Play Protect warns that the app is unrecognised, tap **More details → Install anyway**. It warns because the app isn't from the Play Store.

If there's no release, open the green run in **Actions**, scroll to **Artifacts** at the bottom, and download **Sadhya-apk**. It's a zip with `Sadhya.apk` inside.

Sadhya then appears in your app drawer with the pink heart icon. It opens full screen, with no browser bar, and works offline.

**Updating:** push your changes, wait for the new release, then download and open the new `Sadhya.apk`. It installs over the old app and keeps your ticks. That works because every build is signed with the same key in `android-signing/`, so don't delete that folder.

You can also rebuild without changing anything: **Actions → Build Sadhya APK → Run workflow**.

## 3. Install it on a laptop or iPhone (web app)

1. Go to the repo's **Settings → Pages**.
2. Set **Source** to *Deploy from a branch*, **Branch** to `main`, and the folder to `/ (root)`, then click **Save**.
3. After a minute or two, the app is live at `https://<your-username>.github.io/sadhya/`.

To install it from there:

- **Chrome or Edge (laptop or Android):** click **Install app**. It's in the app's sidebar, in Settings, or in the browser's address bar or menu.
- **iPhone / iPad:** open the link in Safari, tap **Share**, then **Add to Home Screen**.

## Your progress

Ticks are saved on each device. The APK, the laptop app and the website each keep their own copy.

To move progress between devices, use **Settings → Export** on one and **Settings → Import file** or **Paste** on the other. Inside the Android app, Export copies the backup text to your clipboard; paste it into a note or chat to keep it.

To preview carry-over, use **Settings → Treat today as** and pick a later date. Choose **Use real date** to go back.

## Changing the plan

Edit `Placement_DayWise_Plan.xlsx`, keeping the same sheet names and columns. Then, from this folder, run:

```bash
pip install openpyxl
python tools/extract_plan.py
```

That rebuilds `index.html`. Next, change `VERSION` in `sw.js` (for example to `sadhya-v2`) so installed web apps pick up the update. Finally, commit and push. GitHub builds a fresh APK, and Pages updates the web version.

Ticks are linked to each topic's `#` number and the order of its tasks. Moving a topic to another date keeps its ticks, but reordering tasks inside a topic can shift them.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole app: layout, styles, data and logic |
| `manifest.webmanifest` | App name, colours and icons for installing |
| `sw.js` | Lets the app open offline and be installed |
| `icons/` | App icons (home screen, maskable, Apple, favicon) |
| `android-res/` | Ready-made Android launcher icons and splash screen |
| `COPY-ME-build-apk.yml` | Visible copy of the build workflow, for pasting in if `.github` didn't upload |
| `.github/workflows/build-apk.yml` | Builds `Sadhya.apk` on GitHub and publishes it as a release |
| `package.json`, `capacitor.config.json` | Android app wrapper settings (app id `com.payal.sadhya`) |
| `android-signing/sadhya.keystore` | Fixed signing key so updates install over the old app |
| `Placement_DayWise_Plan.xlsx` | The source plan |
| `tools/extract_plan.py`, `tools/template.html` | Rebuild `index.html` from the sheet |
