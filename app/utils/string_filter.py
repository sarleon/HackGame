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

#过滤on事件
def on_event_sub_filter(input_string):
    return re.sub('on\d+','onevent',input_string)


#过滤js schmea
def javascript_schema_filter(input_string):
    return re.sub('javascript:','javascript',input_string)


def expression_filter(input_string):
    return re.sub('expression:','expression',input_string)


