from django.shortcuts import render, redirect

def login_view(request):
    # Simply renders the login design
    return render(request, 'login.html', {'hide_header_footer': True})

def register_view(request):
    # Simply renders the registration design
    return render(request, 'register.html', {'hide_header_footer': True})

def logout_view(request):
    # Simply redirects back to home page
    return redirect('index')

def user_profile_view(request):
    # Mock data to demonstrate order lists and dashboard elements visually
    mock_orders = [
        {
            'id': 'ORD-98241',
            'date': 'June 15, 2026',
            'total': '154.99',
            'status': 'Shipped',
            'status_class': 'bg-success bg-opacity-10 text-success',
            'items': 'Leather Backpack x1, Water Bottle x1'
        },
        {
            'id': 'ORD-97103',
            'date': 'May 20, 2026',
            'total': '89.90',
            'status': 'Delivered',
            'status_class': 'bg-primary bg-opacity-10 text-primary',
            'items': 'Mechanical Keyboard x1'
        }
    ]
    
    # If a real user is logged in, use their credentials. 
    # Otherwise, populate with design dummy user so the profile page isn't blank.
    user_context = request.user if request.user.is_authenticated else {
        'username': 'Alex_Ecom',
        'email': 'alex@fastecom.com',
        'first_name': 'Alex',
        'last_name': 'Smith',
        'date_joined': '2026-06-19'
    }
    
    context = {
        'orders': mock_orders,
        'user': user_context
    }
    return render(request, 'user_profile.html', context)

def admin_profile_view(request):
    # Mock admin dashboard metrics and activity feed context
    context = {
        'total_sales': '12,450.00',
        'total_orders': 84,
        'total_users': 42,
        'pending_orders': 8,
        'recent_orders': [
            {'id': 'ORD-98241', 'user': 'john_doe', 'date': 'June 15, 2026', 'total': '154.99', 'status': 'Pending', 'status_class': 'badge bg-warning text-dark'},
            {'id': 'ORD-98239', 'user': 'alice_smith', 'date': 'June 14, 2026', 'total': '199.99', 'status': 'Processing', 'status_class': 'badge bg-info text-dark'},
            {'id': 'ORD-98235', 'user': 'bob_jones', 'date': 'June 12, 2026', 'total': '34.99', 'status': 'Shipped', 'status_class': 'badge bg-success'},
        ]
    }
    return render(request, 'admin_profile.html', context)
