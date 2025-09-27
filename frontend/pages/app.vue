<template>
<Transition
    leave-active-class="transition-all duration-1000 ease-in-out"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
>
    <div v-if="pageLoading" class="fixed inset-0 z-50 bg-black">
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
    <div v-if="!pageLoading" class="overflow-x-hidden pb-10">
        <video src="/media/backgrounds/landscapeapp.mp4" autoplay muted loop playsinline class="object-cover h-[30vh] lg:h-[50vh]  w-full rounded-b-3xl"/>

        <router-link to="/">
            <div class="absolute z-10 text-center text-white top-4 left-4">
                <Icon name="lets-icons:back" class="font-bold text-4xl sm:text-5xl md:text-6xl xl:text-7xl 2xl:text-8xl transition-transform duration-700 ease-in-out hover:rotate-[-360deg]"></Icon>
            </div>
        </router-link>


        <div class="m-4 lg:m-6 z-10 -mt-10 lg:-mt-10  flex flex-col">
            <textarea v-model="url"  placeholder="Paste any URL and get an AI-powered summary in seconds!" class="w-full h-[10vh] rounded-lg p-4 focus:outline-none shadow-md shadow-neutral-900 text-center text-md lg:text-lg xl:text-xl 2xl:text-2xl resize-none"></textarea>

            <button class="btn mt-6 mb-8 md:mb-12  2xl:mb-24 w-fit mx-auto" @click="sendUrl">
                <svg height="24" width="24" fill="#FFFFFF" viewBox="0 0 24 24" data-name="Layer 1" id="Layer_1" class="sparkle">
                <path d="M10,21.236,6.755,14.745.264,11.5,6.755,8.255,10,1.764l3.245,6.491L19.736,11.5l-6.491,3.245ZM18,21l1.5,3L21,21l3-1.5L21,18l-1.5-3L18,18l-3,1.5ZM19.333,4.667,20.5,7l1.167-2.333L24,3.5,21.667,2.333,20.5,0,19.333,2.333,17,3.5Z"></path>
                </svg>

                <span class="text">Generate</span>
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
</Transition>
</template>

<script setup lang="ts">
const pageLoading = ref(true)
let isLoading = ref<boolean | null>(null)
const url = ref<string>('')
const summary = ref<string>('')
const title = ref<string>('')

onMounted(() => {
setTimeout(() => {
    pageLoading.value = false
}, 3000)
})

async function sendUrl() {
    if (url.value != ''){
        isLoading.value = false
        try {
            const response = await fetch('https://neuroclip-bdjb.onrender.com/summaryGeneration', {
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



        .btn {
        border: none;
        width: 15em;
        height: 5em;
        border-radius: 3em;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        background: #1C1A1C;
        cursor: pointer;
        transition: all 450ms ease-in-out;
    }

    .sparkle {
        fill: #AAAAAA;
        transition: all 800ms ease;
    }

    .text {
        font-weight: 600;
        color: #AAAAAA;
        font-size: medium;
    }

    .btn:hover {
        background: linear-gradient(0deg,#A47CF3,#231F77);
        box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.4),
        inset 0px -4px 0px 0px rgba(0, 0, 0, 0.2),
        0px 0px 0px 4px rgba(255, 255, 255, 0.2),
        0px 0px 180px 0px #231F77;
        transform: translateY(-2px);
    }

    .btn:hover .text {
        color: white;
    }

    .btn:hover .sparkle {
        fill: white;
        transform: scale(1.2);
    }
</style>