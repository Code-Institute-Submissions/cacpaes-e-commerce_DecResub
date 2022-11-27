from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def bag_contents(request):

    bag_items = []
    total = 0
    book_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            book = get_object_or_404(Book, pk=item_id)
            total += item_data * book.price
            book_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'book': book,
            })
        else:
            book = get_object_or_404(Book, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * book.price
                book_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'book': book,
                    'size': size,
                })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
