const btn = document.getElementById('dark-btn');

btn.addEventListener('click', () => {
    // 1. Jalankan fungsi toggle class dark-mode pada body
    document.body.classList.toggle('dark-mode');

    // 2. Efek visual tambahan: Membuat ikon petir di dalam tombol ikut bereaksi
    const icon = btn.querySelector('i');
    if (icon) {
        if (document.body.classList.contains('dark-mode')) {
            // Saat mode super gelap aktif (System Overdrive)
            icon.classList.remove('fa-bolt');
            icon.classList.add('fa-power-off'); // Berubah jadi ikon power off/on
            btn.style.boxShadow = '0 0 15px #ff0055'; // Pendaran tombol berubah merah neon
            btn.style.borderColor = '#ff0055';
            btn.style.color = '#ff0055';
        } else {
            // Saat kembali ke mode deep space normal
            icon.classList.remove('fa-power-off');
            icon.classList.add('fa-bolt'); // Kembali jadi ikon petir
            btn.style.boxShadow = '0 0 5px rgba(0, 242, 254, 0.3)'; // Kembali ke cyan neon
            btn.style.borderColor = '#00f2fe';
            btn.style.color = '#00f2fe';
            btn.style.background = 'transparent';
        }
    }
});