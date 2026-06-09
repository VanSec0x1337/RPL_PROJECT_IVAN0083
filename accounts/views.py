from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    """
    View untuk login pengguna.
    Mengautentikasi username dan password, kemudian membuat session.
    Jika berhasil, redirect ke halaman daftar mahasiswa.
    Jika gagal, tampilkan pesan error.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validasi input
        if not username or not password:
            messages.error(request, 'Username dan password harus diisi!')
        else:
            # Autentikasi user
            user = authenticate(
                request,
                username=username,
                password=password
            )
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Selamat Datang, {user.username}')
                # Redirect ke halaman next atau halaman utama mahasiswa
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('index')
            else:
                messages.error(
                    request,
                    'Username atau password salah!'
                )
    
    # Cek apakah user di-redirect dari halaman yang memerlukan login
    next_url = request.GET.get('next')
    if next_url:
        messages.info(request, 'Login dulu!')
    
    context = {'next': next_url}
    return render(request, 'accounts/login.html', context)


@login_required(login_url='/accounts/login/')
def logout_view(request):
    """
    View untuk logout pengguna.
    Menghapus session dan redirect ke halaman login.
    """
    auth_logout(request)
    messages.success(request, 'Anda berhasil logout!')
    return redirect('accounts:login')

