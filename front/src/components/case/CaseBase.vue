<template>
  <el-row>
    <el-col :span="3">
      <el-menu  :default-active="$route.path" router>
        <el-menu-item index="/case">用例</el-menu-item>
        <el-menu-item index="/case/group">分组</el-menu-item>
        <el-menu-item index="/case/script">脚本</el-menu-item>
        <el-menu-item index="/case/mock">数据</el-menu-item>
        <el-menu-item index="/case/result">结果</el-menu-item>
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