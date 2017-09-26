from django.core.paginator import Paginator

'''4个参数：全量数据，当前页，一页显示数量，展示页数'''
def paginate_queryset(objs, page_no, cnt_per_page=10, half_show_length=3):
	p = Paginator(objs, cnt_per_page)
	if page_no > p.num_pages:	#想要的当前页>总页数
		page_no = p.num_pages
	if page_no <= 0:	#想要的当前页<=0
		page_no = 1
	page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1)        #标页列表
                  if i > 0 and i <= p.num_pages]
	page = p.page(page_no)                  #提取第几页：参数page_no是GET的参数
	previous_link = page_links[0]-1			#最小页-1
	next_link = page_links[-1]+1          	#最大页+1
	has_previous = previous_link > 0		#有前页
	has_next = next_link <= p.num_pages		#有后叶
	pagination_data = {"has_previous":has_previous, 'has_next':has_next,
						'previous_link':previous_link, 'next_link':next_link,
						'page_cnt':p.num_pages, 'current_no':page_no,
						'page_links':page_links}
	return (page.object_list, pagination_data)		#返回当前页数据，7个参数字典


