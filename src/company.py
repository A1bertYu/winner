import re

class Company:

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self._stock_id, self._name, self._category_code or "",
        self._category_name or "", self._subcategory_code or "", self._subcategory_name or "",
        self._class_code or "", self._class_name or "")

    @property
    def stock_id(self):
        return self._stock_id

    @stock_id.setter
    def stock_id(self, stock_id):
        self._stock_id = stock_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    #门类 > 次类 > 大类 > 中类 
    @property
    #门类代码
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        self._category_code = category_code

    #门类名称
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name


    #次类
    @property
    def subcategory_code(self):
        return self._subcategory_code

    @subcategory_code.setter
    def subcategory_code(self, subcategory_code):
        self._subcategory_code = subcategory_code

    @property
    def subcategory_name(self):
        return self._subcategory_name

    @subcategory_name.setter
    def subcategory_name(self, subcategory_name):
        self._subcategory_name = subcategory_name

    #大类
    @property
    def class_code(self):
        return self._class_code

    @class_code.setter
    def class_code(self, class_code):
        self._class_code = class_code

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        self._class_name = class_name
    
    def load(self, company_info):
        self._stock_id = company_info[0]
        self._name = company_info[1]
        if company_info[2] is not None:
            self._category_code = company_info[2]
        if company_info[3] is not None:
            self._category_name = company_info[3]

        if company_info[4] is not None:
            self._subcategory_code = company_info[4]
        if company_info[5] is not None:
            self._subcategory_name = company_info[5]

        if company_info[6] is not None:
            self._class_code = company_info[6]
        if company_info[7] is not None:
            self._class_name = company_info[7]

    @staticmethod
    def parse(file_path):
        result = []
        with open(file_path, 'r') as company_file:
            company_info = []
            #the below 4 variables is used to find a class/categroy name which takes up 2 lines
            #in "company_list.txt"
            #e.g. 电力、热力、燃气及水生
            #     产和供应业
            # we need to use "replace" of NotePad to make a name only occupy 1 line
            line_no1 = 0
            line_no2 = -1
            last_line = ""
            last_stock_id = ""
            for line in company_file:
                line = line.strip()
                info_len = len(company_info)

                if 0 < info_len and info_len < 8:
                    company_info.append(line)
                elif info_len == 8:
                    info_len = 0
                    company = Company()
                    company.load(company_info)
                    result.append(company)
                    company_info = []

                if info_len == 0:
                    if len(line) == 6 and re.fullmatch("[0-9]{6}", line):
                        company_info.append(line)
                        if line_no2 != -1 and (line_no1 - line_no2) != 8 and last_line != "大类简称":
                                print ("The number of lines occupied by this stock (id={}) is not 8.".format(last_stock_id))
                        line_no2 = line_no1
                        last_stock_id = line
                line_no1 = line_no1 + 1
                last_line = line
        return result
                