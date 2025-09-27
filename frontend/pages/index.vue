<template>
<Transition
    leave-active-class="transition-all duration-1000 ease-in-out"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
>
    <div v-if="isLoading" class="fixed inset-0 z-50 bg-black">
    <video 
        src="/media/backgrounds/loadingvideo.mp4" 
        autoplay 
        muted 
        loop 
        playsinline 
        class="w-full h-full object-cover"
    />
    </div>
</Transition>

<Transition
    enter-active-class="transition-all duration-800 ease-out"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
>
    <div v-if="!isLoading" class="m-4 lg:m-6 overflow-x-hidden">
    <video src="/media/backgrounds/heroBackground.mp4" autoplay muted loop playsinline class="object-cover h-[95vh] w-full rounded-3xl"/>
    <div class="absolute z-10 text-center text-white top-10 left-14">
        <h1 class="font-bold text-4xl sm:text-5xl md:text-6xl xl:text-7xl 2xl:text-8xl italic">NeuroClip</h1>
    </div>
    <div class="absolute z-10 flex flex-col gap-4 text-left px-8 text-white bottom-40 left-8">
        <h1 class="font-bold text-5xl sm:text-7xl md:text-8xl lg:text-9xl xl:text-7xl 2xl:text-9xl">Read Less, Learn More</h1>
        <p class="italic text-sm sm:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl w-[70%]">Paste any URL and get an AI-powered summary in seconds. Perfect for researchers, students, and professionals who need to process information quickly and efficiently.</p>
    </div>
    <div class="absolute inset-0 z-10 flex text-white px-16 py-12 items-end">
        <NuxtLink to="/app">
        <button class="text-white italic font-semibold rounded-full text-2xl sm:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl flex items-center gap-4">Get started
            <Icon name="material-symbols:arrow-forward"></Icon>
        </button>
        </NuxtLink>
    </div>
    <div class="h-fit flex flex-col md:flex-row gap-4 mt-14">
        <div class="card md:w-[50%]">
        <div class="flex flex-row gap-2">
            <Icon name="clarity:child-arrow-line" class="text-7xl flex items-start h-10"></Icon>
            <div class="flex flex-col gap-2">
            <h1 class="font-bold text-xl sm:text-2xl md:text-3xl lg:text-4xl 2xl:text-5xl text-neutral-900">
                Tired reading long articles?</h1>
            <p class="italic text-sm lg:text-lg 2xl:text-xl xl:px-12 2xl:px-16">We can summarize any article in seconds. Perfect for busy professionals and students who need to process information quickly and efficiently.</p>
            </div>
        </div>
        </div>
        <div class="card md:w-[50%]">
        <div class="flex flex-row gap-2">
            <Icon name="clarity:child-arrow-line" class="text-9xl flex items-start h-10"></Icon>
            <div class="flex flex-col gap-2">
            <h1 class="font-bold text-xl sm:text-2xl md:text-3xl lg:text-4xl 2xl:text-5xl text-neutral-900">
                Stop Drowning in Information</h1>
            <p class="italic text-sm lg:text-lg 2xl:text-xl xl:px-12 2xl:px-16">Tired of bookmarking articles you'll never read? End the endless scroll of overwhelming content that leaves you feeling behind. Our AI cuts through the noise to deliver only what matters, so you can finally tackle that reading list without the guilt or time pressure.</p>
            </div>
        </div>
        </div>
    </div>
    <div class="h-fit py-10">
        <h1 class="mx-auto text-center font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl 2xl:text-8xl flex items-center justify-center pb-4 lg:pb-10">
        See it in action!
        </h1>
        <video src="/media/backgrounds/demo.mp4" controls muted class="w-full h-auto object-cover rounded-3xl my-10"></video>
    </div>
    </div>
</Transition>
</template>

<script setup lang="ts">
const isLoading = ref(true)

onMounted(() => {
setTimeout(() => {
    isLoading.value = false
}, 3000)
})
</script>

<style scoped>
</style>