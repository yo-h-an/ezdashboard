class WrapperDashboard():
    def __init__(self,**kwargs):
        self._CSS_BASE = get_base_css()
        self._list_id=[]
        self._width_default = kwargs.get('width_default',15)
        self.css = None
        self.js=None
        self.header=None
        self.misc = None 
        self.dic_tabs=None
        self.dashboard=None
        self.html_dashboard_content = None
        self._disclaimers_kind= kwargs.get('disclaimers_kind','us')
    
    def init_dashboard(self,title=None,tabs=[],widgets_state=[]):
        for attr in ['css','js','header','misc']:
            assert self._getattribute_(attr)
        title = title or self.make_title('To be Changed')
        self.dashboard = Dashboard(**{'title': title,
                         'css': self.css,
                         'js': self.js,
                         'misc': self.misc,
                         'header': self.header,
                         'markdown': False,
                         'widgets': False,
                         'widgets_state': widgets_state,
                         'latex': True
                        })
        
        if isinstance(tabs,list):
            for i,tab in enumerate(tabs):
                self.add_tab(tab,str(i),i)
        
        elif isinstance(tabs,dict):
            for i,item in enumerate(tabs,dict):
                k,tab = item
                self.add_tab(tab,k,i)
    
    @staticmethod
    def embed_image_data(image_path,alt="",extend_width = False,center=False):
        with open(image_path, "rb") as image_file:
            # Read and encode the image
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
            extendwidth = '' if not extend_width else 'width:100vm;'
            # Generate and return HTML with the Base64-encoded image
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Embedded Image</title>
            </head>
            <body>
                <h1>Embedded Image</h1>
                <img src="data:image/jpeg;base64,{base64_string}" alt="Embedded Image" style="{extendwidth}">
            </body>
            </html>
            """
        if center:
            html = '<center>' + html + '</center>'
        return html
    
    def make_slide_tab_with_one_image(self,image_path,tab_name,title = None,active=False,disclaimers=None):
        html_image = self.embed_image_data(image_path,extend_width = True)
        dic_slide ={
            'disclaimers':{'text':disclaimers},
        } if disclaimers is not None else {}
        
        
        dic_slide = {
            'title':{'name':title},
            **dic_slide
        }if title is not None else dic_slide
        
        dic_slide = {
            **dic_slide,
            'row1':{
                'li_li_htmls':[[html_image]],
                'with_borders':False,
            },
        }
        
        tab = self.make_slide_from_dict(dic_slide,tab_name,active=active)
        
        return tab
    
    
    def make_slide_tab_from_dict(self,dic_slide,tab_name,active=False):
        
        dic_title = dic_slide.pop('title',False)
        if dic_title:
            title_elmt = self.make_title(dic_title['name'],size = dic_title.get('size',4))
        else:
            title_elmt = None
            
        dic_disclaimers = dic_slide.pop('disclaimers',False)
        if dic_diclaimers:
            disclaimers_elmt = self.make_disclaimers_styled_row(dic_diclaimers.get('text','Source: MS'))
        else:
            disclaimers_elmt = None
            
        elmts = []
        for _, dic_row in dic_slide.items():
            li_li_htmls = dic_row.pop('li_li_htmls',[[]])
            row = self.make_equal_row_from_li_htmls(li_lil_htmls,**dic_row)
            elmts.append(row)
            
        elmts = [title_elmts] + elms if title_elmts else elmts
        elmts = elms + [dic_disclaimers] if dic_disclaimers else elmts
        
        return self.make_tab(elmts,name= tab_name,active=False)
    
    def make_disclaimers_styled_row(self, text_disclaimers):
        html = text_disclaimers #change to have to appropriate formatting
        row = self.make_equal_row_from_li_htmls([[html]])
        return row 
    
    def make_vertical_list_dic_from_html(self,li_htmls:iter):
        elmts=[]
        for html in li_htmls:
            div = self.make_div(html,width=12,**kwargs)
            elmts.append(div)
        li_div = 
        pass
    
    
    def make_row_from_one_html(self,li_li_htmls:iter,li_width = None,**kwargs):
        div = self.make_div(content,id_name,class_name,width,with_borders,is_markdown,**kwargs)
        li_divs = self.make_list_div([div])
        return self.make_row(li_div)
    
    def make_equal_row_from_li_htmls(self,li_li_htmls:iter,li_width=None,**kwargs):
        assert all(isinstance(e,list) for e in li_li_htmls)
        if li_width is None:
            n=len(li_li_htmls)
            li_width = [12//n]*n
        else:
            asser len(li_width)==len(li_li_htmls)
        
        elmts=[]
        for li_htmls,width in zip(li_li_htmls,li_width):
            li_div_temp = self.make_vertical_list_div_from_htmls(li_htmls,width =width,**kwargs)
            elmts.append(li_div_temp)
        
        li_div = self.make_list_div(elmts,level=1)
        return self.make_row(li_div)
    
    def __get_new_default_id(self):
        new_id = len(self._list_id)
        while new_id in self._list_id:
            new_id+=1
        return new_id
    
    def __update_width(self,width,dic):
        if width is None:
            if self._width_default is None:
                dic.pop('width')
            else:
                dic.update({'width':self._width_default})
        return dic
    
    def get_css(self,css=None):
        if css is not None:
            self.css = self._CSS_BASE +css
        else:
            self.css = self._CSS_BASE
    
    def get_js_scripts(self):
        self.js=None
    
    def make_div(self,content,id_name_None,class_name='div_default'):
        dic_attributes = locals()
        #add str widget sats
        widgets_state = kwargs.get('widgets_state',False)
        if widgets_state:
            self.dashboard.widget_state.append(widgets_state)
        #update width
        dic_attributes = self.__update_width(width,dic_attributes)
        #update id_name 
        if id_name is None:
            new_id = self.__get_new_default_id()
            dic_attributes.update({'id_name':new_id})
            self._list_id.append(new_id)
        else:
            self._list_id.append(id_name)
        
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        assert not is_markdown,'markdown not supported'
        
        return Div(**dic_attributes)
    
    def make_list_div(self,elmts:list,width=None,class_name='list_div_default',level=None,**kwargs):
        dic_attributes = locals()
        dic_attributes = self.__update_width(width,dic_attributes)
        if level is None:
            dic_attributes.pop('level')
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        return ListDiv(**dic_attributes)
    
    
    def make_row(self,elmts:ListDiv,class_name='row_default',**kwargs):
        dic_attributes = locals()
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        return Row(**dic_attributes)
    
    def make_tab(self,elmts:list,name:str,class_name='tab_default',level=1,active=False,**kwargs):
        dic_attributes = locals()
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        return Tab(**dic_attributes)
    
    
    def make_title(self,text:str,class_name='title_default',size=4,**kwargs):
        dic_attributes = locals()
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        return Title(**dic_attributes)
    
    def make_diclaimer_tab(self,active=True):
        li_disclaimers = self.make_list_div([self.make_div(get_disclaimers_html(kind=self._disclaimers_kind))],width=12)
        row_disclaimers = self.make_row(li_disclaimers)
        tab_disclaimers = self.make_tab([row_disclaimers],'Disclaimers',active=active)
        return tab_disclaimers
    
    def make_front_page_tab(self,path=None,file_name= 'add_background.jpg',tab_name = 'Strategies',active=True):
        path_image = path
        html_image = self.embed_image_data(path, extend_width =True)
        row = self.make_row_from_one_html(html_image_front_page)
        html_text =""""""
        row_2 = self.make_row_from_one_html(html_text)
        tab = self.make_tab([row,row_2],tab_name,active=active)
        return tab
    
    
    def get_header(self,left_logo = None,right_logo=PATH_MS_LOGO,left_title = "left_title",toggle=False,**kwargs):
        dic_attributes = locals()
        dic_attributes.pop('kwargs')
        dic_attributes.pop('self')
        self.header = Header(**dic_attributes)
        
        
    def get_misc(self):
        self.misc = Misc(**{'main_type':'container-fluid',
                           'main_class_name':'wrapper',
                           'main_nav_width':'17%',
                           'main_nav_min_heigth':'15%',
                           'main_content_width':'82%',
                           'no_margin':False,
                           })
        
    def add_tab(self,tab,name,position=True):
        self.dic_tabs.update({name:tab})
        self.dashbaord.add_tab(tab,position)
        
        
    def remove_tab(self,position):
        tab = self.dasboard.remove_tab(position)
        return tab
    
    def build(self,save_path ="add_path",save=True,save_name:str=None,verbose=True,disclaimers_tab=True,
             front_page_tab='active',front_page_file_name:'str' = 'front_page_background.JPG',tab_name_front_page= 'presentation'):
        if save_name is None:
            save_name = "Dashboard"
        save_name = save_name.replace('html','')+'.html'
        assert self.dashboard is not None,'DAshboard not initialised'
        
        if disclaimers_tab and 'disclaimers' not in self.dic_tab.keys():
            self.add_tab(self.make_disclaiemr_tab(active = disclaimers_tab =='active'),'disclaimers')
        elif not disclaimers_tab and 'disclaimers' in self.dic_tabs.keys():
            self.remove_tab(position=-1)
        if front_page_tab and 'front_page' not in self.dic_tab.keys():
            self.add_tab(self.make_front_page_tab(path=None,file_name =front_page_file_name,tab_name=tab_name_front_page,active=front_page_tab=='active'), 'front_page',0)
        elif not front_page_tab and 'front_page' in self.dic_tabs.keys():
            self.remove_tab(position =0)
            
        self.dashboard.run(verbose=verbose)
        self.html_dashboard_content = self.dashboard.build(save=save,save_path=save_path,save_name=save_name,verbose=verbose)

data_grouping = kwargs.get('data_grouping',False)



g = hc.Highstock()
colors_default_line = __default_colors()
dic_visible = {c: c not in kwargs.get('hidden',[]) for j,c in enumerate(df.columns)}
g.series = hc.build.series(df,colors=dic_color, visible = dic_visible, lineWidth = lineWidth, secondary_y = secondary_y, type= dic_type_chart)
g.yAxis = [
    {'opposite':False,
    'labels':{'style':{'fontSize':17}}
    },
    {'opposite':True,
    'labels':{'style':{'fontSize':17}}}
]
g.plotOptions.series.dataGrouping.enabled = data_grouping
g.plotOptions.line.marker.enabled = markers
if markers:
    g.plotOptions.line.marker.radius =5
g.legend.enabled = True
g.legend.align ='center'
g.legend.maxHeigth =100
g.exporting.enabled = exporting
# g.exporting.buttons.contextButton.menuItems =['list opts']
g.navigator.enabled = navigator
if not full_size:
    g.chart.width = kwargs.get('width':1220/1.25)
g.chart.height = kwargs.get('height':710)
g.chart.zoomType = 'x'
if title:
    g.title.text=title
if subtitle:
    g.subtitle.text=subtitle
g.plotOptions.series.connectNulls = True

if rebase:
    g.plotOptions.series.compare = 'percent'
    g.plotOptions.series.compareStart = True
    for axis in g.yaxis:
        axis.setdefault('labels',{})['formatter'] =scripts.FORMATTER_PERCENT_REBASE
for axis in g.yAxis:
    axis.setdefault('gridLineWidth',1)
    axis.setdefault('gridLineDashStyle','Dot')

if y_axis_format:
    for axis in g.yAxis:
        axis.setdefault('labels',{})['format'] = y_axis_format
if y_axis_text:
    for axis in g.yAxis:
        axis.setdefault('title',{})['text'] = y_axis_text

g.xAxis.gridLineWidth = 1.0
g.xAxis.gridLineDashStyle ='Dot'

## add format, text,type,vert zero doted line


g.xAxis.labels.style.fontSize = 17
g.tooltip.enabled = tooltip_enabled
g.tooltip.valueDecimals =2 
if rebase:
    g.tooltip.pointFormat = scripts.TOOLTIP_POINT_FORMAT_PERCENT
    g.tooltip.positionner = scripts.TOOLTIP_POSITIONER_CENTER_TOP
else:
    g.tooltip.pointFormatter = scripts.TOOLTIP_POINT_FORMATTER_QUANTILE
    if (add_table='perc' or percent_y_axis):
        for axis in g.yAxis:
            axis.setdefault('labels',{})['formatter'] = scripts.FORMATTER_PERCENT
g.credits_enabled = credits_enabled
g.credits.text = "from {} to {}".format(dk.index[0],df.index[-1])

if kwargs.get('return_object',False):
    return g

if add_table = 'perf':
    html = g.plot_with_table_1(save=save, version=_VERSION,save_path=save_path,notebook=True,dated=save_dated)
elif add_table = 'perf1b':
    html = g.plot_with_table_3(save=save, version=_VERSION,save_path=save_path,notebook=True,dated=save_dated)
elif add_table = 'perc':
    html = g.plot_with_table_2(save=save, version=_VERSION,save_path=save_path,notebook=True,dated=save_dated)
else:
    html = g.plot(save=save, version=_VERSION,save_path=save_path,notebook=True,dated=save_dated)
if display:
    display(HTML(html))
return html


    
    
