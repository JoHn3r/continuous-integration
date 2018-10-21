ressourceName=$1

mkdir -p $ressourceName/group_vars
mkdir $ressourceName/roles

touch $ressourceName/hosts
touch $ressourceName/site.yml
touch $ressourceName/README.md
