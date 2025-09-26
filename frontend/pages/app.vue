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
        </div>
    </div>


</template>

<script setup lang="ts">
let isLoading = ref<boolean | null>(null)
const url = ref<string>('')
const summary = ref<string>('')
const title = ref<string>('')

async function sendUrl() {
    isLoading.value = false
        
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
}

console.log(title)

</script>

<style scoped>

</style>