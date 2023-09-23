### How to fork a repository

1. Navigate to the [GitHub repository](https://github.com/RWallan/carol-app-monitor.git){target="_blank" .external-link}
1. In the top-right corner of the page, click **Fork**

    ![image](https://user-images.githubusercontent.com/70775844/236096629-f8e91279-f5c8-4e52-989d-029d082700a2.png){.center}

1. Under "Owner" select the dropdown menu and click an owner for the forked repository.
1. You can rename the forked repository or mantain the same name of original repository.
1. You can write a description to your forked repository and set/unset the option "Copy the `main` branch only". By default, this option is marked, but you can desmark and clone all branches existing in repository.

### Cloning your forked repository

After you forked the CarolApp Monitor repository:

1. Navigate to **your fork** of the CarolApp Monitor repository
1. Get your repository HTTPS link

1. Open Git Bash or your preferred terminal
1. Go to the location where you want the cloned repository
1. Type `git clone` and paste **your github URL**

#### Example of cloning a repository

<!-- termynal -->

```
$ git clone https://github.com/RWallan/carol-app-monitor.git
Cloning into 'carol-app-monitor' ...
remote: Enumerating objects: 116, done.
remote: Counting objects: 100% (116/116), done.
remote: Compressing objects: 100% (71/71), done.
Receiving objects:  58% (68/116)used 109 (delta 33), pack-reused 0
Receiving objects: 100% (116/116), 307.36 KiB | 2.13 MiB/s, done.
Resolving deltas: 100% (40/40), done.
```

!!! tip "Using VsCode to clone repository"
    You can use an IDE like VisualStudioCode to clone the repository by point and click. In this [documentation](https://code.visualstudio.com/blogs/2021/06/10/remote-repositories){target="_blank" .external-link} you can read more about it.
