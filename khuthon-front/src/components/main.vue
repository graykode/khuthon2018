<template>
    <div id="mainWrapper">
        <div id="section1">
            <searchFrom></searchFrom>
            <wordcloud></wordcloud>
        </div>
        <div id="section2">
            <rank></rank>
        </div>
    </div>
</template>

<script>
import searchFrom from './searchForm'
import wordcloud from './wordcloud'
import rank from './rank'

export default {
    components:{
        searchFrom,
        wordcloud,
        rank
    }
}
</script>

<style>
#mainWrapper{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 100vh;
}
#section1{
    flex-grow: 7;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
#section1 > :nth-child(1){
    flex-grow: 1;
}
#section1 > :nth-child(2){
    flex-grow: 8;
}
#section2{
    flex-grow: 1
}
</style>
