<template>
    <div >
        <div>
            <h1 class="header1">AI-powered summaries to optimize your researches!</h1>
            <p class="paragraph text-center my-6 mx-2">From long websites to short summary - Use AI to optimize your workflow</p>

            <div class="flex flex-col sm:flex-row  gap-4 justify-center items-center">
                <NuxtLink to="/app" class="button text-white bg-neutral-900 text-xl">Start now</NuxtLink>
                <button class="button text-lg">Play Demo</button>
            </div>

            <NuxtImg src="/undraws/undraw_knowledge_0ty5.svg"  class="w-full h-[40vh] sm:h-[60vh] lg:h-[75vh]  mx-auto mt-20"/>
        </div>

        <div class="h-fit mt-20">
            <h1 class="header1 my-16">Optimize your time</h1>

            <div class="flex flex-col gap-20">
                <card1 media="/undraws/undraw_artificial-intelligence_43qa.svg" title="AI creates summary, you save time" description="Just paste the URL and get a summary in seconds. No manual work - just quick and effective summaries for your learning and documenting."></card1>

                <card1 media="/undraws/undraw_save-to-bookmarks_9o51.svg" title="Save and Organize Your Summaries" description="Keep all your summaries in one place. Search through your history and access them anytime. Build your personal knowledge library effortlessly."></card1>

                <card1 media="/undraws/undraw_group-chat_4xw0.svg" title="Multi-Language Support" description="Summarize content in any language and get results in your preferred language. Break language barriers and access global content effortlessly."></card1>

                <card1 media="/undraws/undraw_share-link_y9oh.svg" title="Export and Share Anywhere" description="Download your summaries as PDF, copy to clipboard, or share directly via link. Take your summaries wherever you need them - docs, notes, emails, or presentations."></card1>
            </div>
        </div>

        <div class="h-fit mt-20">
            <h1 class="header1 my-16 text-left">Made for Students, Content Creators, Busy Professionals</h1>

            <div class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-3  gap-12">
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
                    <p class="paragraph text-left">Sign up in seconds and start using BrieflyAI for free. Get instant access to AI-powered quizzes without any commitments or setup.</p>
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

                <div class="flex flex-col sm:flex-row  gap-4 items-start">
                    <NuxtLink to="/app" class="button text-white bg-neutral-900 text-xl">Start now</NuxtLink>
                <button class="button text-lg">Play Demo</button>
            </div>
            </div>
        </div>
    </div>
</template>



<script setup lang="ts">

</script>
