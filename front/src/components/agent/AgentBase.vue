<template>
  <el-row>
    <el-col :span="3">
      <el-menu  :default-active="$route.path" router>
        <el-menu-item index="/agent">代理机</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="21" class="container">
        <router-view></router-view>
    </el-col>
  </el-row>
</template>

<style>
  .container{
    padding:10px;
  }
</style>