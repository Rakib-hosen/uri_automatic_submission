#conda activate "C:\Users\ASUS TUF GAMING\Documents\python projects\myenv"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
import time
user = "humanphysiology06@gmail.com"
pwd = "11111111"
class uri:
    def __init__(self,user,pwd):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        self.driver = webdriver.Firefox(capabilities=cap,executable_path="geckodriver.exe")
        self.user= user
        self.pwd= pwd
        
        
    def login(self):
        #global driver
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/login")
        assert "URI Online Judge" in self.driver.title
        elem = self.driver.find_element_by_id("email")
        elem.send_keys(self.user)
        elem = self.driver.find_element_by_id("password")
        elem.send_keys(self.pwd)
        elem.send_keys(Keys.RETURN)
        #print(self.user,self.pwd)
        time.sleep(2)
        
    def submit(self,problem):
        gb=""
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/runs/add/"+problem)
        obj = Select(self.driver.find_element_by_name("language_id"))
        obj.select_by_value("2")
        textarea= self.driver.find_element_by_xpath('//*[@id="editor"]/textarea')
        textarea.clear()
        try:
            with open('problems/uri '+problem+'.cpp','r') as f:
                gb=f.read()
        except:
            pass
        #print(gb)
        textarea.send_keys(gb)
        sendb= self.driver.find_element_by_xpath('//*[@id="element"]/form/div[5]/input')
        sendb.click()
        time.sleep(2)
        
        
    def lasttry(self):
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/runs")
        prblmresults = self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr[1]/td[5]/a').text
        prblmname= self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr[1]/td[4]/a').text
        prblmid=self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr[1]/td[3]/a').text
        prblmlanguge=self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr[1]/td[6]').text
        prblmdate=self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr[1]/td[8]').text
        print(prblmname)
        print(prblmid)
        print(prblmlanguge)
        print(prblmresults)
        print(prblmdate)
        
        
    def solved(self):
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/account")
        accnt_id = self.driver.find_element_by_xpath('//*[@id="identification"]')
        accnt_id = accnt_id.get_attribute('value')
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/users/statistics/"+accnt_id)
        time.sleep(3)
        solved_prblm=self.driver.find_element_by_xpath('//*[@id="st-solved"]').text
        print("solved problems :" + str(solved_prblm))
        
        
    def ques_solved(self):
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/runs?answer_id=1&page=1")
        acpage = self.driver.find_element_by_xpath('//*[@id="table-info"]').text
        _,_,l=acpage.split()
        print( "solved problems  : id, name")
        #print(l)
        for j in range(1,int(l)+1):
            self.driver.get("https://www.urionlinejudge.com.br/judge/en/runs?answer_id=1&page="+str(j))
            for i in range(1,29):
                try:
                    prblmid=self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr['+str(i)+']/td[3]/a').text
                    prblmname= self.driver.find_element_by_xpath('//*[@id="element"]/table/tbody/tr['+str(i)+']/td[4]/a').text
                    print(prblmid,prblmname)
                except:
                    break
            


#a= uri(user,pwd)
#a.login()
#a.submit("1003")
#a.lasttry()
#a.solved()
#a.ques_solved()
#time.sleep(60)
#driver.close()