<template>
  <el-row>
    <el-col :span="2">
      <h3>logo</h3>
    </el-col>
    <el-col :span="22">
      <el-menu mode="horizontal" router menu-trigger="click"> 
        <el-menu-item index="/me">工作台</el-menu-item>
        <el-menu-item index="/project">项目</el-menu-item>
        <el-menu-item index="/case">用例</el-menu-item>
        <el-menu-item index="/agent">代理</el-menu-item>
        <el-menu-item index="/org">组织</el-menu-item>
        <el-menu-item index="/timeline">图</el-menu-item>
        <el-submenu index="6" :style="{float:'right'}">
           <template slot="title">当前账号</template>
             <el-menu-item index="/message">信息</el-menu-item>
             <el-menu-item index="/profile">设置</el-menu-item>
             <el-menu-item index="/help">帮助</el-menu-item>
             <el-menu-item index="6-3" @click.native="logout">退出</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-col>
    <el-col :span="24" class="container">
      <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return {
      }
    },
    methods:{
      logout(){
        var _this = this
        this.$confirm('确定要退出系统吗').then(()=>{
          sessionStorage.removeItem('usertoken')
          _this.$router.push('/')
        }).catch(()=>{
          
        })
      }
    }
  }
</script>
<style>
  .header{
    background: #20a0ff;
    padding:0px;
  }
  .container{
    padding:10px;
  }
</style>