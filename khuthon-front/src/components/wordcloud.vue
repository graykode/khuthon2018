<template>
    <div>
        <wordcloud
            :data="defaultWords"
            nameKey="name"
            valueKey="value"
        >
        </wordcloud>
    </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'

export default {
    name: 'app',
    components: {
        wordcloud
    },
    data() {
        return {
            defaultWords: [{'name':'test','value':100}, {'name':'test','value':50}, {'name':'test','value':10}]
        }
    },
    methods:{
        addWords(name, value){
            this.defaultWords.push({
                name,
                value
            })
        }
    }
}
</script>