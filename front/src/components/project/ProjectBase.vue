<template>
  <el-row>
    <el-col :span="3">
      <el-menu  :default-active="$route.path" router>
        <el-menu-item index="/module/1">项目模块</el-menu-item>
        <el-menu-item index="/api/list/1">接口列表</el-menu-item>
        <el-menu-item index="/projectmember/1">成员列表</el-menu-item>
        <el-menu-item index="/host/1">环境配置</el-menu-item>
        <el-menu-item index="/code/1">状态码</el-menu-item>
        <el-menu-item index="/log/1">项目动态</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="21" class="container">
        <router-view></router-view>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
      }
    }
  }
</script>
<style>
  .container{
    padding:10px;
  }
</style>