#!/usr/bin/python3
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts=response_dict['items']
#print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
#repo_dict=repo_dicts[0]
#print("\nKeys:",len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
#print("\nSelected information about each repository:")
#for repo_dict in repo_dicts:
#    print('\nName:',repo_dict['name'])
#    print('Owner:',repo_dict['owner']['login'])
#    print('Stars:',repo_dict['stargazers_count'])
#    print('Repository:',repo_dict['html_url'])
#    print('Description:',repo_dict['description'])

#处理结果
#print(response_dict.keys())

names,plot_dicts=[],[]
#names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict={
            'value':repo_dict['stargazers_count'],
            'label':repo_dict['description'],
        }
        plot_dicts.append(plot_dict)
    else:
        plot_dict={
            'value':repo_dict['stargazers_count'],
            'label':'ABC',
        }
        plot_dicts.append(plot_dict)
#    stars.append(repo_dict['stargazers_count'])
#可视化
my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')

