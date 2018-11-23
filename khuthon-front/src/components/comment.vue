<template>
    <div id="commentWrapper">
        <div class="comment" v-for="comment in comments" :key="comment.id">
            <div>
                <i class="fas fa-user-circle" v-bind:class="{'male' : !comment.gender, 'female' : comment.gender}"></i>
                <div> {{comment.user}} </div>
            </div>
            <div>
                {{comment.comment}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            comments : [
                {'id' : 1, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 0},
                {'id' : 2, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 1},
                {'id' : 3, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 1},
                {'id' : 4, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 0},
                {'id' : 5, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 0},
                {'id' : 6, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 1},
                {'id' : 7, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 1},
                {'id' : 8, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 0},
                {'id' : 9, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 1},
                {'id' : 10, 'user' : 'test', 'comment' : 'testcomment', 'gender' : 0},
            ]
        }
    }
}
</script>

<style>
#commentWrapper{
    height: 100%;
    background: #ffffff;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
 
    overflow: scroll;
    
}
.comment{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    margin-top: 15px;
    width: 90%;
    min-height: 100px;
    box-shadow: 0 4px 8px 0 rgba(173, 75, 75, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.comment > :nth-child(1){
    width: 20%;

    display: flex;
    flex-direction: column;
}
.fa-user-circle{
    font-size: 60px;
}
.male{
    color: #00ffff;
}
.female{
    color: #ff00aa;
}

.comment > :nth-child(2){
    width: 70%;

    display: flex;
    flex-direction: column;
}

</style>
