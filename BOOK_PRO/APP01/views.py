from django.shortcuts import render,HttpResponse
from APP01 import models
# Create your views here.

def index(request):
    #一对一 增
    # new_author_detail=models.AuthorDetail.objects.create(
    #     birthday='1994-2-22',
    #     telephone='13222222',
    #     addr='杭州22',
    # )
    # # print(new_author_detail)
    # obj=models.AuthorDetail.objects.filter(addr='杭州22').first()
    # models.Author.objects.create(
    #     name='陆22',
    #     age='25',
    #     # authorDetail=new_author_detail
    #     authorDetail_id=obj.nid
    # )

    #一对多 增
    # obj=models.Publish.objects.get(nid=2)
    # models.Book.objects.create(
    #     title='大话2',
    #     publishDate='2020-1-1',
    #     price=20,
    #     # publish=obj
    #     # publish=models.Publish.objects.get(nid=2)
    #     publish_id=obj.nid
    # )


    #多对多
    # book_obj=models.Book.objects.get(nid=3)
    # book_obj.authors.add(*[3,5])

    # author1=models.Author.objects.get(nid=3)
    # author2=models.Author.objects.get(nid=5)
    # book_obj=models.Book.objects.get(nid=1)
    # book_obj.authors.add(*[author1,author2])


    # return render(request,'index.html')

    #删
    #一对一 删
    # models.AuthorDetail.objects.get(nid=3).delete()

    #一对多 删
    # models.Publish.objects.get(nid=1).delete()

    #多对多 删
    # book_obj=models.Book.objects.get(nid=1)
    # # book_obj.authors.remove(5)
    # # book_obj.authors.remove(*[5,6])
    # # book_obj.authors.clear()
    # # book_obj.authors.add(*[5,])
    # book_obj.authors.set(['1','5'])#删除后 更新

    #更新
    #一对一 更新
    models.Author.objects.filter(nid=1).update(
        name='陆威',
        age=18,
        # authorDetail=models.AuthorDetail.objects.get(nid=1),
        # authorDetail_id=3,
    )
    #一对多
    models.Book.objects.filter(pk=4).update(
        title='大话2',
        pulish_id=2,

    )
    #没有级联更新 ， 会报错
    return HttpResponse('OKOKOK')