import requests


def get_github(id):
    url_repository = "https://api.github.com/users/" + id + "/repos"
    repository_name = []
    number_commit = []
    request_repository = requests.get(url_repository)
    list_repositoy = request_repository.json()
    '''
    check  the repository if exist and the ID if exist   
    '''
    if list_repositoy == []:
        NewId= input('There is no repository in this' + id +' Please try to input another Id\n')
        get_github(NewId)
    else:
        if 'message' in list_repositoy:
            NewId = input('The user ' + id +' is not exist. Please try to input another Id\n' )
            get_github(NewId)
    for i in list_repositoy:
        repository_name.append(i['name'])
    #print(repository_name)

    for name in repository_name:
        url_commit = 'https://api.github.com/repos/' + id + '/' + name + '/commits'
        request_commit = requests.get(url_commit)
        list_commit = request_commit.json()
        number_commit.append(len(list_commit))
    #print(number_commit)
    res = []
    for s in range(0,len(repository_name)):
        res.append('Repo: ' + repository_name[s] + ' Number of commits: ' + str(number_commit[s]))
    # print(res)
    return res

if __name__ == '__main__':
    ID = input('Please input the Github Id\n')
    res = get_github(ID)
    for i in res:
        print(i)
