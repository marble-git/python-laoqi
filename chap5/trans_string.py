#coding:utf-8

'''
    filename:trans_string.py
        chap:5
    subject:16
    conditions:string_msg,mode_choice
    solution:transformed string
'''




msg = 'Laoqi QQ group:26913719'

def trans_string(target:'target elements',mode:'transform mode'=None):
    '''mode choices:
        None:do nothing,
        private:echo <target>with *,
        delete:delete <target>,
        keep:delete chars not in <target>
    '''
    all_chars = ''.join(chr(i) for i in range(20,0xff))
    #print(all_chars)
    if mode is None:
        trans_table=str.maketrans('','')
    elif 'private'.startswith(mode):
        trans_table=str.maketrans(target,'*'*len(target))
    elif 'delete'.startswith(mode):
        trans_table=str.maketrans('','',target)
    elif 'keep'.startswith(mode):
        trans_table=str.maketrans('','',all_chars)
        trans_table.update(str.maketrans(target,target))
    else:
        #print('unsupported mode,try <None,private,delete,keep>.')
        #trans_table={}
        raise ValueError('Unsupported <mode>')
    
    def inner(origin:'origin string'):
        return origin.translate(trans_table)

    return inner



        
numbers = '0123456789'
modes = [None,'pri','del','k','l']

for mode in modes:
    trans = trans_string(numbers,mode)
    print(f'mode {mode} :',trans(msg))
