from django.contrib import admin

# Register your models here.
from support.models import Faq, Inquiry, Category, Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    # 리스트 화면에서 보일 필드
    list_display = ('id', 'title', 'updated_at', )
    # 자동으로 갱신되어 수정할 수 없는 필드들 볼 수 있게
    readonly_fields = ('created_at', 'updated_at',)
    # 검색 필드
    search_fields = ('title',)
    # 필터 필드
    list_filter = ('category', )

# Inquiry 한 객체에 answer list가 들어갈 수 있도록 class 생성
class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변'
    readonly_fields = ('created_at', 'updated_at',)

@admin.action(description='선택한 문의가 답변 완료 상태로 변경됩니다.')
def make_completed(modeladmin, request, queryset):

    # status 필드를 답변 완료 상태로 update
    queryset.update(status='c')

    # queryset의 values 중에서 phone_reply를 dictionary 형태로 가져와서 첫 번쩨 원소의 phone_reply key값으로 value에 접근하여 참인지 비교
    if (queryset.values('phone_reply')[0]['phone_reply'] == True):
        #  queryset의 values 중에서 phone을 dictionary 형태로 가져와서 첫 번쩨 원소의 phone key값으로 value에 접근
        print(queryset.values('phone')[0]['phone'])

    # queryset의 values 중에서 email_reply dictionary 형태로 가져와서 첫 번쩨 원소의 email_reply key값으로 value에 접근하여 참인지 비교
    if (queryset.values('email_reply')[0]['email_reply'] == True):
        #  queryset의 values 중에서 email을 dictionary 형태로 가져와서 첫 번쩨 원소의 email key값으로 value에 접근
        print(queryset.values('email')[0]['email'])


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    model = Inquiry

    # 리스트 화면에서 보일 필드 + 상태 필드 추가
    list_display = ('id', 'title', 'category', 'created_at', 'writer', 'status',)
    # 자동으로 갱신되어 수정할 수 없는 필드들 볼 수 있게
    readonly_fields = ('created_at', 'updated_at',)

    # 1:1문의 검색 필드 추가
    search_fields = ['writer__username', 'phone', 'email', ]

    # 필터 필드
    list_filter = ('category', )

    inlines = [AnswerInline]

    actions = [make_completed]


# 카테고리 class admin site에 등록
admin.site.register(Category)
