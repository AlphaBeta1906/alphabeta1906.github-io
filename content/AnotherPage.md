Title: Apa itu alpine.js
Category: Framework
keywords: framework,website,frontend,javascript,alpinejs,blogging
header_cover: images/alpine_cover.jpg

Javascript adalah satu satunya bahasa pemograman yang digunakan pada bagian front end website. Dengan javascript developer dapat membuat tampilan dari website menjadi lebih interaktif daripada hanya menggunakan html atau css saja. Saat ini pun sudah sangat banyak framework atau library javascript frontend yang dapat membantu menciptakan tampilan yang interactive dengan mudah tanpa perlu berurusan dengan DOM javascript yang agak rumit. Mulai dari library klasik seperti [JQuery](https://api.jquery.com/) hingga framework fullstack seperti [NextJs](https://nextjs.org/), kita dapat memilih sesuai dengan kebutuhan. Nah disini saya akan memperkenalkan framework Js yang ringan dan mungkin juga bakal disukai oleh developer back end yang kadang jarang menggunakan javascript (backend diluar node js ya...), yaitu **Alpine Js**

# Apa itu Alpine js?
Alpine js adalah framework javascript ringan(hanya 8kb!) yang membantu membuat html kita lebih interaktif dan dinamis. Framework ini pertama kali dirilis oleh Caleb Porzio pada 29 Nov 2019 dengan 0.1.0 sebagai versi pertama dan baru menjadi versi 1.0 pada  19 Dec 2019. Alpine js umumnya digunakan sebagai tambahan untuk membuat html lebih interaktif dengan mudah dan ringan, makannya framework ini cocok digunakan sebagai pelengkap untuk framewrok fullstack yang menggunakan server side rendering, seperti Django,Flask atau Laravel. Nah, berbeda dengan framework seperti [Vue](https://vuejs.org/guide/introduction.html) atau [Svelte](https://svelte.dev), kita dapat menulis kode Js kita langsung pada tag html  layaknya atribut tag html, berikut adalah contoh sederhananya

<iframe height="300" style="width: 100%;" scrolling="no" title="Untitled" src="https://codepen.io/alphabeta1906/embed/RwyZMRm?default-tab=html&editable=true" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/alphabeta1906/pen/RwyZMRm">
  Untitled</a> by AlphaBeta (<a href="https://codepen.io/alphabeta1906">@alphabeta1906</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

Nah, diatas adalah contoh bagaimana kita dapat membuat sebuah toggle button hanya di dalam html saja, kita juga bisa menyisipkan kode js di dalam atribut dari alpine untuk memanipulasi hasilnya.

# Cara instalasi dan penggunaan sederhana  Alpine js 
Alpine js sangat mudah untuk di install,kita hanya perlu menaruh tag berikut pada bagian head di html
```html
 <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
```
Kita pun langsung dapat menggunakan Alpine dengan menambahkan atribut `x-data` pada  tag yang ingin dijadikan sebagai komponen Alpine, seperti berikut ini

```html
<div x-data>
</div>
```
Setiap tag yang memilki `x-data` (entah itu kosong atau memilki nilai seperti yang di awal) merupakan komponen alpine dan harus ada jika kita ingin menggunakan direktif atau atribut khusus alpine yang lain di dalam blok tag tersebut .Berikut adalah perbandingannya: 

✅ akan muncul text
```html
<div x-data>
   <span x-text="('Halo!')"/>
</div>
```

❌ tidak muncul apa apa, tidak ada `x-data`
```html
<div>
   	<span x-text="('Halo!')"/>	
</div>
```

❌ tidak muncul apa apa, diluar  `x-data`
```html
<div x-data>
</div>
<span x-text="('Halo!')"/>
```

# Atribut khusus dari alpine
Alpine js memiliki 15 atribut khusus, berikut adalah daftarnya

 **x-data**  
`x-data` adalah atribut yang digunakan untuk mendeklarasikan tag menjadi komponen Alpine, kita juga dapat 	menaruh nilai yang hanya dapat diakses oleh tag yang berada di dalam komponen,contoh: 

```html
<div x-data="{test: 'hello'}">
	   <span x-text="test"/>
</div>
```

nah, kode di atas akan memunculkan text 'hello' karena atribut `x-text` mengakses variabel test.

 **x-text**  
atribut ini digunakan untuk menampilkan nilai dalam bentuk text(sama seperti diatas), contoh: 

```html
<div x-data="{test: 'hello ',test2: 'world'}">
	<span x-text="test + test2"/>
</div>
```    


**x-on**  
`x-on ` adalah atribut yang mirip dengan event listener bawaan html, contoh:
```html
<div x-data="{toggle: false}">
    <button x-on:click="toggle = !toggle">
      Munculkan text
    </button>
   <p x-show="toggle">
     Hello world
   </p>
</div>
```

**x-model**  
atribut ini digunakan untuk menyinkronkan sebuah data dengan elemen input, contoh

```html
<div x-data="{ test: ''}">
  <input type="text" x-model="search"> 
  Text: <span x-text="search"></span>
</div>
```

**x-show**  
atribut  ini digunakan untuk mengatur tampil tidak nya sebuah elemen. contoh: 

```html
<div x-show="true">
    Muncul	
</div>
```

**x-bind**  
Atribut yang digunakan untuk membuat atribut html lain menjadi dinamis, contoh: 

```html
<div x-data="{warna: 'biru'}">	
	<div x-bind:class="warna == 'biru' ? 'biru' : ''">
	  ...
	</div>
</div>
```

**x-html**  
hampir sama seperti `x-text` tapi ia akan memunculkan html daripada text biasa
```html
<div x-data="{test: '<h1>Hello</h1> ' }">
    <span x-html="test"/>
</div>
```

**x-transition**  
`x-transition` adalah atribut yang digunakan untuk memberikan efek transisi css untuk elemen yang muncul dan tersembunyi, biasanya digunakan berdampingan dengan `x-show`, contoh: 

```html
<div x-data="{toggle: false}">
    <button x-on:click="toggle = !toggle">
      Munculkan text
    </button>
   <p x-show="toggle" x-transition>
     Hello world
   </p>
</div>
```

**x-cloak**  
atribut yang digunakan untuk menyembunyikan elemen hingga alpine selesai di download di browser, contoh:

```html
<div x-data>
	<div x-cloak>Sembunyi saat loading</div>
	<div>Muncul</div>
</div>
```

**x-for**  
Atribut yang melakukan perulangan pada sebuah elemen, sama seperti for loop pada bahasa pemograman, contoh:

```html
<div x-data="{buahan: ['jeruk','apel','mangga'] }">
<template x-for="buah in buahan">
  <p x-text="buah"></p>
</template>
```
*Note: template hanya bisa memiliki satu elemen saja*

**x-if**  
`x-if` adalah atribut yang memiliki fungsi serupa dengan if statment dan di alpine hampir mirip dengan `x-show`, yaitu akan memunculkan elemen sesuai kondisi,contoh: 

```html
<div x-data="{muncul: 'ya'}">
	
	<template x-if="muncul == 'ya'">
	  <div>muncul</div>
	</template>

</div>
```

**x-init**   
Atribut ini digunakan untuk menginisialisasi data awalan di alpine, contoh: 

```html
<div x-data="{pesan: ''}">
	<div x-init="pesan='halo'"/>
	<span x-text="pesan"/>
</div>
```

**x-effect**  
Atribut yang akan dijalankan jika salah satu nilai di dalamnya berubah,contoh: 

```html
<div x-data="{hitung: 0}">
	<div x- effect="console.log(hitung)">
	</div>
</div>
```

**x-ref**  
`x-ref` adalah atribut yang digunakan untuk merefernsikan elemen langsung menggunakan kata kuncinya, dan dapat diakses menggunakan property `$ref`, contoh:

```html
<div x-data>
	
<input type="text" x-ref="content">
 
<button x on:click="navigator.clipboard.writeText($refs.content.value)">
  Copy
</button>
</div>
```

**x-ignore**  
Atribut yang digunakan untuk mencegah elemen html diinisialisasi oleh alpine, contoh: 

```html
<div x-data>
	<div x-ignore>
		Abaikan
	</div>
</div>
```


Dan itulah penjelasan mengenai Alpine js.