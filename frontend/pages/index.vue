<template>
    <div class="mx-[10%] mb-20">
        <div class="bg-neutral-100 rounded-full px-4 py-2  w-fit mx-auto my-4">
            <div class="flex flex-row gap-2 items-center justify-center">
                <NuxtLink to="/"  class="font-bold text-xl h-full">NEUROCLIP</NuxtLink>
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
                    <div class="flex flex-col gap-4 items-center justify-center text-lg">
                        <NuxtLink to="/Help" class="hover:opacity-50 transition-opacity">Help</NuxtLink>
                        <NuxtLink to="/Pricing" class="hover:opacity-50 transition-opacity">Pricing</NuxtLink>
                        <NuxtLink to="/About" class="hover:opacity-50 transition-opacity">About us</NuxtLink>
                        <NuxtLink to="/FAQ" class="hover:opacity-50 transition-opacity">FAQ</NuxtLink>
                    </div>
                    <div class="flex flex-col gap-4 items-center justify-center">
                        <button class="button bg-white shadow-lg shadow-neutral-900 hover:opacity-75 transition-opacity">LogIn</button>
                        <button class="button bg-neutral-900 text-white shadow-lg shadow-neutral-900 hover:opacity-90 transition-opacity">SignUp</button>
                    </div>
                </div>
            </transition>
        </div>

        <div class="h-fit mt-14">
            <h1 class="header1">AI-powered summaries to optimize your researches!</h1>
            <p class="paragraph text-center my-6 mx-2">From long websites to short summary - Use AI to optimize your workflow</p>

            <div class="flex flex-col gap-4 justify-center items-center">
                <NuxtLink to="/app" class="button text-white bg-neutral-900 text-xl">Start now</NuxtLink>
                <button class="button text-lg">Play Demo</button>
            </div>

            <img src=""  class="w-full h-[50%]">
        </div>

        <div class="h-fit mt-20">
            <h1 class="header1 my-16">Optimize your time</h1>
            <div class="flex flex-col gap-20">
                <div class="flex flex-col gap-2">
                    <div class="wireframe">
                        <img src="" class="object-contain">
                    </div>

                    <div class="flex flex-col gap-2">
                        <h2 class="header2 text-left">AI creates summary, you save time</h2>
                        <p class="paragraph text-left">Just paste the URL and get a summary in seconds. No manual work - just quick and effective summaries for your learning and documenting.</p>
                        <NuxtLink to="/app"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
                    </div>
                </div>

                <div class="flex flex-col gap-2">
                    <div class="wireframe">
                        <img src="" class="object-contain">
                    </div>

                    <div class="flex flex-col gap-2">
                        <h2 class="header2 text-left">Save and Organize Your Summaries</h2>
                        <p class="paragraph text-left">Keep all your summaries in one place. Search through your history and access them anytime. Build your personal knowledge library effortlessly.</p>
                        <NuxtLink to="/app"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
                    </div>
                </div>

                <div class="flex flex-col gap-2">
                    <div class="wireframe">
                        <img src="" class="object-contain">
                    </div>

                    <div class="flex flex-col gap-2">
                        <h2 class="header2 text-left">Multi-Language Support</h2>
                        <p class="paragraph text-left">Summarize content in any language and get results in your preferred language. Break language barriers and access global content effortlessly.</p>
                        <NuxtLink to="/app"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
                    </div>
                </div>

                <div class="flex flex-col gap-2">
                    <div class="wireframe">
                        <img src="" class="object-contain">
                    </div>

                    <div class="flex flex-col gap-2">
                        <h2 class="header2 text-left">Export and Share Anywhere</h2>
                        <p class="paragraph text-left">Download your summaries as PDF, copy to clipboard, or share directly via link. Take your summaries wherever you need them - docs, notes, emails, or presentations.</p>
                        <NuxtLink to="/app"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
                    </div>
                </div>
            </div>
        </div>

        <div class="h-fit mt-20">
            <h1 class="header1 my-16 text-left">Made for Students, Content Creators, Busy Professionals</h1>

            <div class="grid grid-cols-1 gap-12">
                <div class="wireframe h-fit p-8">
                    <h2 class="header2 text-left">Students & Researchers</h2>
                    <p class="paragraph text-left">Digest academic papers, articles, and study materials faster. Spend less time reading, more time learning and writing.</p>
                    <img src="/undraws/undraw_educator.svg" class="mt-12 h-[50%]">
                </div>

                <div class="wireframe h-fit p-8">
                    <h2 class="header2 text-left">Content Creators & Marketers</h2>
                    <p class="paragraph text-left">Stay on top of industry trends and competitor content without the time sink. Gather insights and inspiration efficiently.</p>
                    <img src="/undraws/undraw_content-creator.svg" class="mt-12 h-[50%]">
                </div>

                <div class="wireframe h-fit p-8">
                    <h2 class="header2 text-left">Busy Professionals</h2>
                    <p class="paragraph text-left">Cut through information overload. Get briefed on reports, news, and documentation without sacrificing your productivity.</p>
                    <img src="/undraws/undraw_business-man.svg" class="mt-12 h-[50%]">
                </div>
            </div>

        </div>

        <div class="h-fit mt-20">
            <h1 class="header1 text-left my-16">Get started in 3 steps:</h1>

            <div class="grid grid-cols-1 gap-12">
                <div class="flex flex-col gap-4">
                    <div class="wireframe w-16 h-16 rounded-full flex items-center justify-center text-3xl font-bold">1</div>
                    <h2 class="header2 text-left">Sign up and get started</h2>
                    <p class="paragraph text-left">Sign up in seconds and start using NeuroClip for free. Get instant access to AI-powered quizzes without any commitments or setup.</p>
                </div>

                <div class="flex flex-col gap-4">
                    <div class="wireframe w-16 h-16 rounded-full flex items-center justify-center text-3xl font-bold">2</div>
                    <h2 class="header2 text-left">Summarize your website</h2>
                    <p class="paragraph text-left">Use AI to summarize your website in seconds to make your learning easier.</p>
                </div>

                <div class="flex flex-col gap-4">
                    <div class="wireframe w-16 h-16 rounded-full flex items-center justify-center text-3xl font-bold">3</div>
                    <h2 class="header2 text-left">Start learning</h2>
                    <p class="paragraph text-left">Start learning everything you want in a easier way, share it with friends or team and enjoy your new optimized life.</p>
                </div>

                <div class="flex flex-col gap-4 items-start">
                    <NuxtLink to="/app" class="button text-white bg-neutral-900 text-xl">Start now</NuxtLink>
                <button class="button text-lg">Play Demo</button>
            </div>
            </div>
        </div>
    </div>
</template>



<script setup lang="ts">
const menu = ref<boolean>(false)
</script>
