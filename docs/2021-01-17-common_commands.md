mkdir <dir>
touch <file>
ls <dir/file>
cat <file>
cd <dir>
mv <old_name> <new_name>
[vim]
vim <file>
C = ctrl
自动补全

    C-x C-s -- 拼写建议。
    C-x C-v -- 补全vim选项和命令。
    C-x C-l -- 整行补全。
    C-x C-f -- 自动补全文件路径。弹出菜单后，按C-f循环选择，当然也可以按 C-n和C-p。
    C-x C-p 和C-x C-n -- 用文档中出现过的单词补全当前的词。 直接按C-p和C-n也可以。
    C-x C-o -- 编程时可以补全关键字和函数名啊。
    C-x C-i -- 根据头文件内关键字补全。
    C-x C-d -- 补全宏定义。
    C-x C-n -- 按缓冲区中出现过的关键字补全。 直接按C-n或C-p即可。

当弹出补全菜单后：

    C-p 向前切换成员；
    C-n 向后切换成员；
    C-e 退出下拉菜单，并退回到原来录入的文字；
    C-y 退出下拉菜单，并接受当前选项。
[git]
git
git add <./file>
git commit
git commit --amend      #修改最后一次提交的注释
git reset --hard <HASH> #撤销HASH之后的提交
git log
git log --stat          #显示简单统计信息
git log --oneline       #显示单行提交信息
git log -num            #显示最近num次的提交日志
git clone git@github.com:USER_NAME/REPO_NAME
git pull
git push
