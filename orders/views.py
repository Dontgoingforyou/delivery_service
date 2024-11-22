from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'created':
            return Response(
                {'error': 'Нельзя удалить заявку, которая была передана в доставку или уже доставлена'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def set_status(self, request, pk=None):
        instance = self.get_object()
        new_status = request.data.get('status')
        if new_status not in ['created', 'in_delivery', 'delivered']:
            return Response(
                {'error': 'Некорректный статус'},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.status = new_status
        instance.save()
        return Response({'status': instance.status})