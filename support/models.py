from django.db import models

from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.contrib import admin


# Basic Mission

# FAQ 모델
class Faq(models.Model):

    # 제목 필드
    title = models.CharField(max_length=100, verbose_name="제목")

    # 질문 필드
    question = models.TextField(verbose_name="질문")

    # 상수 선언
    GENERAL = 'GENL'
    ACCOUNT = 'ACCT'
    ETC = 'ETC'

    # 카테고리 튜플 생성
    category_choices = [
        (GENERAL, 'GENERAL'),
        (ACCOUNT, 'ACCOUNT'),
        (ETC, 'ETC'),
    ]

    # 카테고리 필드
    # 필드 내 choices 옵션 이용
    category = models.CharField(max_length=4, choices=category_choices, default='GENL', verbose_name="카테고리")

    # 답변 필드
    answer = models.TextField(verbose_name="답변")

    # 작성자 필드
    writer = models.ForeignKey(User, related_name='faq_create_user', on_delete=models.CASCADE, null=True, blank=True, verbose_name="작성자")
    # 최종 수정자 필드
    modifier = models.ForeignKey(User, related_name='faq_update_user', on_delete=models.CASCADE, null=True, blank=True, verbose_name="최종 수정자")

    # 생성일시 필드
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    # 최종 업데이트 일시 필드
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종 수정 일시")

# Advanced Mission

# 카테고리 모델 정의
class Category(models.Model):

    # 카테고리 이름 필드
    name = models.CharField(max_length=50, unique=True, verbose_name="카테고리")

    # 클래스의 정보를 name으로 호출하는 함수
    def __str__(self):
        return f'{self.name}'


# 문의 상태 튜플 생성
STATUS_CHOICES = [
    ('p', '문의 등록'), # pending
    ('o', '접수 완료'), # on-going
    ('c', '답변 완료'), # completed
]

# Inquiry 모델
class Inquiry(models.Model):
    # 하나의 카테고리에는 여러 개의 글 존재
    # 카테고리 필드
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name="카테고리")

    # 제목 필드
    title = models.CharField(max_length=50, verbose_name="제목")
    # 이메일 필드
    email = models.EmailField(max_length=128, verbose_name="이메일")
    # 이메일 수신 여부 필드
    email_reply = models.BooleanField(default=False, verbose_name="이메일 수신 여부")

    # 휴대폰 번호 유효성 검증
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    # 휴대폰 번호 필드
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = False, verbose_name="전화번호")

    # 번호 수신 여부 필드
    phone_reply = models.BooleanField(default=False, verbose_name="전화 수신 여부")

    # 내용 필드
    content = models.TextField(verbose_name="내용")

    # 파일 필드
    file_upload = models.FileField(upload_to='support/files/%Y/%m/%d/', blank=True, verbose_name="파일")

    # 작성자 필드
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="작성자")

    # 생성일시 필드
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    # 최종 업데이트 일시 필드
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종 수정 일시")

    # 상태 선택 필드 추가
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


# Answer
class Answer(models.Model):
    # 내용
    content = models.TextField(verbose_name="답변")

    # 하나의 문의에는 여러 개의 답변 존재
    inquiry = models.ForeignKey(Inquiry, null=True, blank=True, on_delete=models.CASCADE)

    # 작성자 필드
    writer = models.ForeignKey(User, related_name='answer_create_user', on_delete=models.CASCADE, null=True, blank=True, verbose_name="작성자")

    # 최종 수정자 필드
    updater = models.ForeignKey(User, related_name='answer_update_user', on_delete=models.CASCADE, null=True, blank=True, verbose_name="최종 수정자")

    # 생성일시 필드
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    # 최종 업데이트 일시 필드
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종 수정 일시")










