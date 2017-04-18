## version control with Git

- local VC, single committer
- start with pure command line, no GUI
    - init, status, add, commit, diff, ...
        - diff and long lines don't get along, motivation to keep lines below 100 chars
        max
        - diff and binaries don't get along
- diagram of staging
    - 4 different states: untracked, unmodified, modified, staged
        - commands that transfer between different states
    - git status tells you what state you're in
    - git checkout file to unstage
    - git checkout to some other version
- replace local changes with git checkout -- filename
- mention merges
- can't:
    - can't restore to a version you didn't commit
    - work well with binaries
    - not a backup system!
- when you git init, it handles only what's in that folder (and all its child folders)
- commit messages
- commit early and often, in small logical chunks
    - chunks are not necessarily files, but subsets of files, maybe multiple subsets
    across multiple files
- branches - what are they, why use them?
    - merging, merge conflicts
- GUI for committing and viewing history
    - git-cola, gitx, TortoiseGit, sourcetree
- cloning projects
- git as a kind of high level editor

- pushing to github?
    - can use Github desktop in win and mac
    - using only GH password? key generation? or maybe GH can do that for you now
    - pull requests, allows you to make a contribution without having write access to a
    repo
- gitlab is local equivalent at LRZ, although mostly it's data that's restricted

- psychological reasons for VC:
    - each commit is a nice little reward, gives closure on some feature or fix
    - hard to remember what you've actually done, when you're coding, or editing files in
    general. VC is a way of accounting for the time you've spent sitting on the computer,
    and a way of sharing it with others
- VC gives you an incentive to keep lines shorter than xx characters -- otherwise diffs
are hard to display
- cheat sheet site: http://rogerdudler.github.io/git-guide/

- exercises
    - make repo
    - create and add some files
    - commit
    - change stuff
    - commit again
    - clone something from git(hub), make changes
