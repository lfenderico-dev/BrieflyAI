<template>
    <div class="m-4 lg:m-6">
        <video src="/media/backgrounds/heroBackground2.mp4" autoplay muted loop playsinline class="object-cover h-[95vh] w-full rounded-3xl"/>

        <div class="absolute z-10 flex flex-col gap-4 text-left px-8 text-white bottom-40 left-8">
            <h1 class="font-bold text-5xl sm:text-7xl md:text-8xl lg:text-9xl xl:text-7xl 2xl:text-9xl">Read Less, Learn More</h1>
            <p class="italic text-sm sm:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl w-[70%]">Paste any URL and get an AI-powered summary in seconds. Perfect for researchers, students, and professionals who need to process information quickly and efficiently.</p>
        </div>

        <div class="absolute inset-0 z-10 flex text-white px-16 py-12 items-end">
            <button class="text-white italic font-semibold rounded-full text-2xl sm:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl flex items-center gap-4">Get started
                <Icon name="material-symbols:arrow-forward"></Icon>
            </button>
        </div>

        <div class="h-fit flex flex-row gap-4 my-14">
            <div class="card">
                <h1>Tired of reading long articles?</h1>
                <p>We can summarize any article in seconds. Perfect for busy professionals and students who need to process information quickly and efficiently.</p>
            </div>
        </div>

        <div class="h-fit py-12 lg:py-32">
            <h1 class="mx-auto text-center font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl 2xl:text-8xl flex items-center justify-center pb-4 lg:pb-10">
                See it in action!
            </h1>
            <video src="/media/backgrounds/heroBackground.mp4" controls muted class="w-full h-auto object-cover rounded-3xl my-10"></video>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>