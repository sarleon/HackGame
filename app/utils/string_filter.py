#coding:utf-8
import re



#单纯过滤 "<script>"标签
def script_tag_filter(input_string):
    return input_string.replace('<script>', '')


#过滤大小写的
def script_tag_nf_filter(input_string):
    return re.sub('<script>', '',input_string,flags=re.L)

#递归过滤大小写的
def script_tag_recursive_filter(input_string):
    pattern=re.compile('<script>',re.L)
    while re.search(pattern, input_string) is not None:
        input_string=re.sub('<script>', '',input_string,flags=re.L)
    return input_string




