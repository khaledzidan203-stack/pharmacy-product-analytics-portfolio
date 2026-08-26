# GitHub Upload and GitHub Pages

## Recommended repository name
`pharmacy-product-analytics-portfolio`

## Option A — Git command line (recommended)
1. Create a new **public** repository on GitHub with the name above.
2. Do **not** initialize the remote repository with a README, `.gitignore`, or license because these files already exist locally.
3. Extract the ZIP and open a terminal inside the repository folder.
4. Run:

```bash
git init
git add .
git commit -m "Initial portfolio release"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pharmacy-product-analytics-portfolio.git
git push -u origin main
```

If GitHub prompts for authentication, use GitHub's supported browser/credential-manager flow or GitHub CLI rather than placing a token in repository files.

## Option B — GitHub CLI
From the extracted repository folder:

```bash
git init
git add .
git commit -m "Initial portfolio release"
git branch -M main
gh repo create pharmacy-product-analytics-portfolio --public --source=. --remote=origin --push
```

## Enable the interactive dashboard with GitHub Pages
1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch **main** and folder **/(root)**.
5. Click **Save**.

The root `index.html` will become the portfolio dashboard site. The dashboard reads the checked-in synthetic CSV, so no server-side database is required.

## Recommended repository description
`End-to-end pharmacy product analytics portfolio using synthetic data, Excel, SQL Server, Power BI/DAX, Python validation, and an interactive HTML dashboard.`

## Recommended topics
`data-analytics`, `business-analysis`, `power-bi`, `sql-server`, `excel`, `power-query`, `dax`, `javascript`, `dashboard`, `portfolio-project`
