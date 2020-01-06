'''
@Time    : 2019/12/26 11:43
@Author  : fzj
@Desc    : 小乐同学（智能问答）
'''

from poium import Page, PageElement

class Xiaolepage(Page):
    send_loc = PageElement(class_name='send_btn')
    input_loc = PageElement(class_name='inputQuertion')
    question_loc = PageElement(xpath='/html/body/div[1]/div/div/div[4]/div/div[2]/div[2]/div[7]/div/div/p[2]')
    suggest_loc = PageElement(xpath='/html/body/div[1]/div/div/div[4]/div/div[2]/div[2]/div[7]/div/div/p[3]')

    def question(self,qa):
        #提问
        self.question_loc.click()
        self.input_loc = qa
        self.send_loc.click()

    def suggest(self):
        #提建议
        pass
