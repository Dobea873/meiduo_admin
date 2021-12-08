from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import date
from users.models import User


class UserCountView(APIView):
    """
        用户总量统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self,request):
        # 1.获取当天日期
        now_date = date.today()
        # 2.获取用户总量
        count = User.objects.all().count()
        # 3.返回结果
        return Response({
            'date':now_date,
            'count':count
        })


class UserDayCountView(APIView):
    """
        日增用户统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self,request):
        # 1.获取当天日期
        now_date = date.today()
        # 2.获取当天注册用户总量
        count = User.objects.filter(date_joined__gte=now_date).count()
        # 3.返回结果
        return Response({
            'date':now_date,
            'count':count
        })