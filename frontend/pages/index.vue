<template>
    <div class="m-4 lg:m-6">
        <video src="/assets/backgrounds/heroBackground.mp4" autoplay muted loop playsinline class="object-cover h-[95vh] w-full rounded-3xl"/>

        <div class="absolute inset-0 z-10 flex flex-col gap-4 text-center px-8 text-white top-32">
            <h1 class="font-bold text-5xl sm:text-7xl md:text-8xl lg:text-9xl xl:text-7xl 2xl:text-9xl">Read Less, Learn More</h1>
            <p class="italic text-sm sm:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl lg:px-10 xl:px-20 2xl:px-40">Paste any URL and get an AI-powered summary in seconds. Perfect for researchers, students, and professionals who need to process information quickly and efficiently.</p>
        </div>

        <div class="absolute inset-0 z-10 flex text-white px-16 py-12 items-end">
            <button class="text-white italic font-semibold rounded-full text-2xl sm:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl flex items-center gap-4">Get started
                <Icon name="material-symbols:arrow-forward"></Icon>
            </button>
        </div>

        <div class="h-fit py-12 lg:py-32">
            <h1 class="mx-auto text-center font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl 2xl:text-8xl flex items-center justify-center pb-4 lg:pb-10">
                <Icon name="fxemoji:down"></Icon>
                See it in action!
                <Icon name="fxemoji:down"></Icon>
            </h1>
            <video src="/assets/backgrounds/heroBackground.mp4" controls muted class="w-full h-auto object-cover rounded-3xl my-10"></video>
            <h2 class="mx-auto font-bold text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl flex justify-sart pb-4  lg:pb-10">How does that work?</h2>
            <ul class="text-lg md:text-xl lg:text-2xl xl:text-3xl list-disc mx-4 lg:mx-6">
                <li>Paste your URL</li>
                <li>Wait for the AI to process the information</li>
                <li>Get your result!</li>
            </ul>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>