# **JBT-KBBI**

```

     ██╗██████╗ ████████╗██╗  ██╗██████╗ ██████╗ ██╗
     ██║██╔══██╗╚══██╔══╝██║ ██╔╝██╔══██╗██╔══██╗██║
     ██║██████╦╝   ██║   █████═╝ ██████╦╝██████╦╝██║
██╗  ██║██╔══██╗   ██║   ██╔═██╗ ██╔══██╗██╔══██╗██║
╚█████╔╝██████╦╝   ██║   ██║ ╚██╗██████╦╝██████╦╝██║
 ╚════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝
```

# _JUST BASIC TERMINAL KBBI_

Program Kamus Besar Bahasa Indonesia Offline berbasis Terminal menggunakan bahasa Python sebagai final project untuk mata kuliah Praktikum Struktur Data di Semester 3.

By:

-   [Hans Rio Alfredo Pala](https://github.com/hanpalla) <2008561030>
-   [I Komang Surya Adinandika](https://github.com/suryaadi44) <2008561040>
-   [I Made Alit Darma Putra](https://github.com/alitdarmaputra) <2008561045>
-   [Gusti Ngurah Deva Wirandana Putra](https://github.com/rahdeva) <2008561050>
-   [I Made Juniandika](https://github.com/juniade) <2008561055>

---

## Overview

Program ini mengimplementasikan konsep hashmap untuk menyimpan kata dan artinya pada memori. Hashmap ini menggunakan open chaining sebagai collision resolver. Dimana chaining tersebut berupa tree yang akan menyimpan kata dan masing masing artinya.

---

## Implemented Concepts

### Modul Wajib
> ####  Searching
> Searching merupakan modul utama yang digunakan kelompok ini. Konsep ini diterapkan pada pencarian binary search kata pada chain hash table dan linear search untuk pencarian user pada fungsi login.

> #### Sorting
> Secara tidak langsung, modul ini digunakan ketika melakukan pemasukan data ke binary tree yang dapat menghasilkan daftar kata yang terurut.

> #### Queue
> Queue diterapkan pada history kata yang dicari oleh pengguna.

### Modul Pilihan

> #### Hashing
> Struktur data hashing digunakan untuk menyimpan tiap kata dan artinya sesuai huruf awal kata yang dipisahkan menjadi 26 ruang tabel. Hash Map yang digunakan menggunakan collision resolver chaining menggunakan struktur data Tree.

> #### Tree
> Struktur data Tree diimplemntasikan pada chain untuk collision resolver dari hash map.

> #### Recursive
> Banyak fungsi mengimplementasikan konsep rekursif, contohnya pada searching dan inserting data pada Tree.

---

## Supported Feature

Fitur-fitur yang ada sejauh ini:

- [x] Search.
- [x] History.
- [x] Login.
- [x] Register.
- [x] Add Kata. 
- [x] Edit Kata. 
- [x] Delete Kata.

---

## Requirements

Modul modul yang dibutuhkan sebelum menjalankan program.

> ### Python3
>
> Install python dari `https://www.python.org/downloads/`

> ### Pip
>
> Cek instalasi pi dengan menjalankan `pip -h`

> ### Rich Library
>
> Digunakan untuk formatting teks pada terminal, dapat di install dengan
> `pip install rich`

---

## Copyright

Project ini mengandung kamus kata dasar yang telah diubah dan berasal dari [KBBI Qt](https://github.com/bgli/kbbi-qt/) dengan lisensi [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
