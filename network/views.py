from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from network.models import Link, Product
from network.serializers import LinkSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    """Функция для создания, редактирования и удаления продукта, а также
        просмотра всего списка продуктов и просмотра отдельного продукта

    Args:
        viewsets (_type_): _description_
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class LinkCreateAPIView(generics.CreateAPIView):
    """Функция для создания цепочки сети

    Args:
        generics (_type_): _description_
    """
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]


class LinkListAPIView(generics.ListAPIView):
    """Функция для просмотра списка всех цепочкек сети

    Args:
        generics (_type_): _description_
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_fields = ['country',]


class LinkRetrieveView(generics.RetrieveAPIView):
    """Функция для просмотра одной отдельной цепочки сети

    Args:
        generics (_type_): _description_
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkUpdateView(generics.UpdateAPIView):
    """Функция для редактирования цепочки сети
    Args:
        generics (_type_): _description_
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkDestroyView(generics.DestroyAPIView):
    """Функция для удаления цепочки сети

    Args:
        generics (_type_): _description_
    """
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


@permission_required('network.clear_debt')
def set_clear_debt(request, pk):
    """Функция для удаления задолженности перед поставщиком

    Args:
        request (_type_): _description_
        pk (_type_): _description_
    """
    debt = get_object_or_404(Link, pk=pk)
    if debt.debt:
        debt.debt = 0
    debt.save()
