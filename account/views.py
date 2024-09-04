from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions, generics, views
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *


class SendCode(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request) -> Response:
        try:
            mobile: str = request.data['mobile']

            user, create_user = User.objects.get_or_create(username=mobile)
            user = user if user else create_user

            code, create_code = PhoneCode.objects.get_or_create(user=user)
            code = code if code else create_code

            if code.is_active and code.expire_date > time_now():
                return Response({'message': 'کد قبلا ارسال شده', 'time_to_expire': (code.expire_date - time_now())},
                                status=status.HTTP_200_OK)

            PhoneCode.objects.filter(expire_date__lte=time_now()).update(is_active=False)

            code.is_active = True
            # code.code = generate_code()  # for generate code
            code.code = '12345'
            code.expire_date = time_now() + 20
            code.save()

            return Response({'message': 'کد ارسال شد', 'time_to_expire': (code.expire_date - time_now())},
                            status=status.HTTP_200_OK)


        except KeyError:
            return Response({'message': 'اطلاعات ورودی را درست تکمیل کنید'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckCode(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request) -> Response:
        try:
            mobile = request.data['mobile']
            code = request.data['code']

            user = User.objects.get(username=mobile)
            if user.phonecode.code != code:
                return Response({'message': 'کد نادرست است'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            if user.phonecode.expire_date < time_now():
                return Response({'message': 'کد منقضی شده است'}, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)

            return Response({'access': str(refresh.access_token), 'refresh': str(refresh)}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'message': 'کاربر وجود ندارد'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except KeyError:
            return Response({'message': 'اطلاعات ورودی را درست تکمیل کنید'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetails(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
