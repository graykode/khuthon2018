<template>
    <div id="mainWrapper">
        <div id="section1">
            <searchFrom></searchFrom> 
            <wordcloud></wordcloud>
        </div>
        <div id="section2">
            <detail></detail>
        </div>
    </div>
</template>

<script>
import eventBus from '../commons/eventBus'

import searchFrom from './searchForm'
import wordcloud from './wordcloud'
import detail from './detail'

export default {
    components:{
        searchFrom,
        wordcloud,
        detail
    },
    created(){
        eventBus.$on("submit", (data)=>{
            console.log(data);
        })
    }
}
</script>

<style>
#mainWrapper{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    
    height: 100%;
    padding: 15px 30px;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    background-image: url("../assets/background2.png");
}
#section1{
    width: 65%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
#section1 > :nth-child(1){
    height: 7%;
}
#section1 > :nth-child(2){
    height: 90%;
}
#section2{
    width: 25%;
}

</style>
