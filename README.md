# Placement Pipeline

A day-wise tracker for placement prep, 9 to 30 October 2026. Every task comes from the plan's
**Sufficient resource** columns and is a checkbox. Add-on resources are left out on purpose.

- **Today**: a date strip, then Conceptual and Coding tabs. Coding is split into *DSA / SQL practice* and *ML / DL coding & projects*.
- **Carry-over**: anything not fully ticked on its day moves to the top of today in red until it's done.
- **Plan**: every topic by date, with search and filters (area, track, priority, status).
- **Insights**: overall %, due-so-far %, streak, days left, remaining work vs plan, activity calendar, and date-wise, area-wise, track and priority breakdowns.
- **Settings**: theme, export / import progress, clear progress.

The whole app is one `index.html`. There is no build step and no server.

## Put it on GitHub Pages (no command line)

1. Sign in at github.com, click **New repository**, name it `placement-pipeline`, choose **Public**, and create it.
2. On the empty repo page, click **uploading an existing file**. Drag in everything from this folder, including the `tools` folder, then click **Commit changes**.
3. Go to **Settings → Pages**. Under *Build and deployment*, set **Source** to *Deploy from a branch*, **Branch** to `main`, and the folder to `/ (root)`. Click **Save**.
4. After a minute or two, the tracker is live at `https://<your-username>.github.io/placement-pipeline/`.

Your file picker may hide `.nojekyll`. It's optional, and the site works without it.

## Or with git

```bash
cd placement-pipeline
git init
git add .
git commit -m "Placement Pipeline tracker"
git branch -M main
git remote add origin https://github.com/<your-username>/placement-pipeline.git
git push -u origin main
```

Then turn on Pages as in step 3 above.

## Your progress

Ticks are saved in the browser you use, so they survive refreshes and redeploys.

- To move to another device or browser, use **Settings → Export** on the old one and **Settings → Import** on the new one.
- Export a backup now and then, because clearing browser data wipes the saved ticks.
- To preview carry-over, use **Settings → Treat today as** and pick a later date. Choose **Use real date** to go back.

## Changing the plan

Edit `Placement_DayWise_Plan.xlsx`, keeping the same sheet names and columns. Then, from this folder, run:

```bash
pip install openpyxl
python tools/extract_plan.py
```

That rebuilds `index.html` with the new topics. Commit and push it, or re-upload `index.html` on GitHub.

Ticks are linked to each topic's `#` number and the order of its tasks. Moving a topic to another date keeps its ticks, but reordering tasks inside a topic can shift them.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app: layout, styles, data and logic |
| `.nojekyll` | Tells GitHub Pages to serve files as they are |
| `Placement_DayWise_Plan.xlsx` | The source plan |
| `tools/extract_plan.py` | Reads the sheet and rebuilds `index.html` |
| `tools/template.html` | The app template the script fills in |
