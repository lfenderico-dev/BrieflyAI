<template>
    <div class="overflow-x-hidden pb-10">
        <video src="/media/backgrounds/landscapeapp.mp4" autoplay muted loop playsinline class="object-cover h-[30vh] lg:h-[50vh]  w-full rounded-b-3xl"/>

        <router-link to="/">
            <div class="absolute z-10 text-center text-white top-4 left-4">
                <Icon name="lets-icons:back" class="font-bold text-4xl sm:text-5xl md:text-6xl xl:text-7xl 2xl:text-8xl italic"></Icon>
            </div>
        </router-link>


        <div class="m-4 lg:m-6 z-10 -mt-10 lg:-mt-10  flex flex-col">
            <textarea v-model="url"  placeholder="Paste any URL and get an AI-powered summary in seconds!" class="w-full h-[10vh] rounded-lg p-4 focus:outline-none shadow-md shadow-neutral-900 text-center text-md lg:text-lg xl:text-xl 2xl:text-2xl resize-none"></textarea>

            <button @click="sendUrl"   class="mt-6 mb-8 md:mb-12  2xl:mb-24 button w-fit mx-auto text-md md:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl bg-neutral-900">
                Get the summary!
            </button>

            <div class="card" v-if="isLoading == true">
                <h1 class="font-bold  text-xl sm:text-2xl md:text-3xl lg:text-4xl 2xl:text-5xl text-center">{{ title }}</h1>
                <p class="italic text-sm lg:text-lg 2xl:text-xl">{{ summary }}</p>
            </div>

            <div v-if="isLoading == false"  class="loader-wrapper flex mx-auto">
                <span class="loader-letter">G</span>
                <span class="loader-letter">e</span>
                <span class="loader-letter">n</span>
                <span class="loader-letter">e</span>
                <span class="loader-letter">r</span>
                <span class="loader-letter">a</span>
                <span class="loader-letter">t</span>
                <span class="loader-letter">i</span>
                <span class="loader-letter">n</span>
                <span class="loader-letter">g</span>
                <div class="loader"></div>
            </div>
        </div>
    </div>


</template>

<script setup lang="ts">
let isLoading = ref<boolean | null>(null)
const url = ref<string>('')
const summary = ref<string>('')
const title = ref<string>('')

async function sendUrl() {
    if (url.value != ''){
        isLoading.value = false
        try {
            const response = await fetch('http://127.0.0.1:8000/summaryGeneration', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url.value })
            })

            const data = await response.json()

            summary.value = data.Summary
            title.value = data.Title

            isLoading.value = true
        } catch (error) {
            throw new Error('Failed to fetch summary')
        }
    } else{
        title.value = 'Error! Please paste a URL'
        isLoading.value = true
    }
}
</script>

<style scoped>
    .loader-wrapper {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 180px;
        height: 180px;
        font-family: "Inter", sans-serif;
        font-size: 1.2em;
        font-weight: 300;
        color: rgb(0, 0, 0);
        border-radius: 50%;
        background-color: transparent;
        user-select: none;
    }

    .loader {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        aspect-ratio: 1 / 1;
        border-radius: 50%;
        background-color: transparent;
        animation: loader-rotate 2s linear infinite;
        z-index: 0;
    }

    @keyframes loader-rotate {
        0% {
        transform: rotate(90deg);
        box-shadow:
            0 10px 20px 0 #01133B inset,
            0 20px 30px 0 #231F77 inset,
            0 60px 60px 0 #144E7A inset;
        }
        50% {
        transform: rotate(270deg);
        box-shadow:
            0 10px 20px 0 #01133B inset,
            0 20px 10px 0 #231F77 inset,
            0 40px 60px 0 #144E7A inset;
        }
        100% {
        transform: rotate(450deg);
        box-shadow:
            0 10px 20px 0 #231F77 inset,
            0 20px 30px 0 #01133B inset,
            0 60px 60px 0 #144E7A inset;
        }
    }

    .loader-letter {
        display: inline-block;
        opacity: 0.4;
        transform: translateY(0);
        animation: loader-letter-anim 2s infinite;
        z-index: 1;
        border-radius: 50ch;
        border: none;
    }

    .loader-letter:nth-child(1) {
        animation-delay: 0s;
    }
    .loader-letter:nth-child(2) {
        animation-delay: 0.1s;
    }
    .loader-letter:nth-child(3) {
        animation-delay: 0.2s;
    }
    .loader-letter:nth-child(4) {
        animation-delay: 0.3s;
    }
    .loader-letter:nth-child(5) {
        animation-delay: 0.4s;
    }
    .loader-letter:nth-child(6) {
        animation-delay: 0.5s;
    }
    .loader-letter:nth-child(7) {
        animation-delay: 0.6s;
    }
    .loader-letter:nth-child(8) {
        animation-delay: 0.7s;
    }
    .loader-letter:nth-child(9) {
        animation-delay: 0.8s;
    }
    .loader-letter:nth-child(10) {
        animation-delay: 0.9s;
    }

    @keyframes loader-letter-anim {
        0%,
        100% {
        opacity: 0.4;
        transform: translateY(0);
        }
        20% {
        opacity: 1;
        transform: scale(1.15);
        }
        40% {
        opacity: 0.7;
        transform: translateY(0);
        }
    }
</style>