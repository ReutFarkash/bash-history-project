# GitHub Setup

To host your project on GitHub, you need to create a new repository on GitHub and then push your local repository to it.

## 1. Create a new repository on GitHub

1.  Go to [GitHub](https://github.com) and log in to your account.
2.  Click the "+" icon in the top-right corner and select "New repository".
3.  Give your repository a name (e.g., `bash-history-project`).
4.  You can add an optional description.
5.  Choose whether to make the repository public or private.
6.  **Do not** initialize the repository with a README, .gitignore, or license, as you have already created these files.
7.  Click "Create repository".

## 2. Push your local repository to GitHub

Once you have created the new repository on GitHub, you will see a page with instructions on how to push your local repository. You will need to run the following commands in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPOSITORY_NAME` with the name of the repository you created on GitHub.

After running these commands, your local repository will be connected to the remote repository on GitHub, and your files will be pushed to it.