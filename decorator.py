from functools import wraps
from time import sleep

class Color_text:
    '''Description of This Class
這個字典使用 ANSI 來更改terminal中的文字顏色，跳脫字元為 '\\x1b'
Default Color     : 'black'  'red'  'green'  'yellow'  'blue' 'purple'  'blue_green'  'white'
Text type         : Reset all setting :0            Fast flash test   :6 
                    Bold face         :1            Replace FC and BC :7
                    Weaken            :2            Delete line       :9
                    Italic            :3
                    Underline         :4
                    Slow flash text   :5
Variable in Class : fc_dict         #存放前景色對應數字的字典
                    bc_dict         #存放背景色對應數字的字典
Function in Class : 
                    1. chg_color            #更改特定字串的 字形；前景色；背景色
                    2. cancel_all_setting   #取消所有的字形設定
'''
    fc_dict={'black':'30','red':'31','green':'32','yellow':'33','blue':'34','purple':'35','blue_green':'36','white':'37'}
    bc_dict={key:str(int(value)+10) for key,value in fc_dict.items()}
    
    def chg_color(message, fc , bc='' , type='0'):
        '''Function=> 更改特定字串的 字形；前景色；背景色
Default Color     : 'black'  'red'  'green'  'yellow'  'blue' 'purple'  'blue_green'  'white'
Text type         : Reset all setting :0             
                    Bold face         :1            
                    Weaken            :2           
                    Italic            :3
                    Underline         :4
                    Slow flash text   :5
                    Fast flash test   :6
                    Replace FC and BC :7
                    Delete line       :9
Argument=> 
            Required argument: 
                        message(str)  #欲更改顏色的字串
                        fc(str)       #前景色的關鍵字
            Optional argument: 
                        bc(str)  =''  #背景色的關鍵字
                        type(str)='0'
            Return  =>  (str)   #處理完的字串
        '''
        if bc == '':
            return '\x1b['+type+';'+Color_text.fc_dict[fc]+'m'+message+'\x1b[0m'
        else:
            return '\x1b['+type+';'+Color_text.fc_dict[fc]+';'+Color_text.bc_dict[bc]+'m'+message+'\x1b[0m'
    def cancel_all_setting():
        print('\x1b[0m')

#DECORATOR
def implement_time(func):
    @wraps(func) ###IMPORTANT

    def wrap(*arg,**kwarg):
        import time
        start_time = time.time()
        func(*arg,**kwarg)
        print('') 
        print(Color_text.chg_color("="*40,'blue'))
        print(Color_text.chg_color("Execution time: "+ str(time.time()-start_time) ,'blue'))
        print(Color_text.chg_color("="*40,'blue'))
    return wrap

def show_function_name(func):
    @wraps(func) ###IMPORTANT!!
    def FF(*ar,**kwar):
        print(Color_text.chg_color("="*40,'blue'))
        print(Color_text.chg_color("Executing Function: "+ func.__name__ ,'blue'))
        print(Color_text.chg_color("="*40,'blue'))
        return func(*ar,**kwar)
    return FF

def show_function_doc(func):
    @wraps(func)
    def FD(*arg,**kwarg):
        if func.__doc__ != None :
            print(Color_text.chg_color("="*40,'yellow'))
            print(Color_text.chg_color("Document of Function:\n "+ str(func.__doc__) ,'yellow'))
            print(Color_text.chg_color("="*40,'yellow'))
        return func(*arg,*kwarg)
    return FD

# print(Color_text.chg_color('HI TEST','red','black','1'))
@show_function_name
@show_function_doc
@implement_time
def func(s=2):
    '''Document Test!'''
    print('start to sleep for ',s,' seconds')
    sleep(s)

    
if __name__ == '__main__':
    func()