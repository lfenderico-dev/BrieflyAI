<template>
    <div>
        <div class="mx-[10%] mb-20">
            <div class="bg-neutral-100 rounded-full px-4 py-2  w-fit mx-auto my-4">
                <div class="flex flex-row gap-2 items-center justify-center">
                    <NuxtLink to="/"  class="font-bold text-xl h-full">BrieflyAI</NuxtLink>
                    <button @click="menu = !menu" :class="{'bg-neutral-200' : menu == true}"   class="text-4xl h-full flex items-center rounded-full p-2"><Icon name="ic:round-menu"></Icon></button>
                </div>

                <transition
                enter-active-class="transition-all duration-300 ease-out"
                leave-active-class="transition-all duration-200 ease-in"
                enter-from-class="opacity-0 -translate-y-4 scale-95"
                enter-to-class="opacity-100 translate-y-0 scale-100"
                leave-from-class="opacity-100 translate-y-0 scale-100"
                leave-to-class="opacity-0 -translate-y-4 scale-95"
                >
                    <div v-if="menu == true" class="absolute top-24 left-1/2 transform -translate-x-1/2 mt-2 bg-neutral-100/80 backdrop-blur-md rounded-3xl z-50 w-48 h-fit p-8 flex flex-col gap-6">
                        <div class="flex flex-col gap-4 items-center justify-center text-lg xl:text-xl">
                            <!-- <NuxtLink to="/Help" class="hover:opacity-50 transition-opacity">Help</NuxtLink>
                            <NuxtLink to="/Pricing" class="hover:opacity-50 transition-opacity">Pricing</NuxtLink> -->
                            <NuxtLink to="/About" class="hover:opacity-50 transition-opacity">About us</NuxtLink>
                        </div>
                        <div class="flex flex-col gap-4 items-center justify-center">
                            <a href="/authentication"  class="button bg-white shadow-lg shadow-neutral-900 hover:opacity-75 transition-opacity">LogIn</a>
                            <a href="/authentication" class="button bg-neutral-900 text-white shadow-lg shadow-neutral-900 hover:opacity-90 transition-opacity">SignUp</a>
                        </div>
                    </div>
                </transition>
            </div>

            <div class="h-fit mt-14">
                <slot></slot>
            </div>
        </div>

        <footer class="mt-20 bg-neutral-900 text-white py-8 px-4  flex flex-col gap-8">
            <h1 class="header1">Create AI-powered summaries with BrieflyAI!</h1>
            <div class="flex flex-col sm:flex-row  gap-4 justify-center items-center">
                <NuxtLink to="/explaination" class="button text-white bg-neutral-900 text-xl">Read more</NuxtLink>
                <!--<button class="button text-lg">Play Demo</button>-->
            </div>

            <NuxtImg src="/undraws/undraw_researching_5qj6.svg"  class="w-full h-[30vh] sm:h-[50vh] lg:h-[60vh]  mx-auto mt-20"/>

            <div class="flex flex-col justify-start items-start gap-4 text-lg lg:text-xl">
                <!--<NuxtLink to="/Help" class="hover:opacity-50 transition-opacity">Help</NuxtLink>-->
                <!--<NuxtLink to="/Pricing" class="hover:opacity-50 transition-opacity">Pricing</NuxtLink>-->
                <NuxtLink to="/About" class="hover:opacity-50 transition-opacity">About us</NuxtLink>
            </div>

            <div class="flex flex-row gap-8 justify-start items-start text-4xl">
                <Icon name="mdi:instagram"></Icon>
                <Icon name="ic:baseline-tiktok"></Icon>
                <Icon name="mdi:youtube"></Icon>
                <Icon name="ic:baseline-reddit"></Icon>
            </div>

            <div class="flex flex-col gap-2 opacity-50">
                <NuxtLink to="/">Terms of Service</NuxtLink>
                <NuxtLink to="/">Privacy Policy</NuxtLink>
                <p>@BrieflyAI</p>
            </div>
        </footer>
    </div>
</template>

<script setup lang="ts">
const menu = ref<boolean>(false)
</script>
