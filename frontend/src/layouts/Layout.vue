<template>
  <div class="common-layout">
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="display: flex; flex: 1; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img src="@/assets/imgs/logo.png" alt="Logo" style="width: 40px" />
          <div style="margin-left: 5px">智能实验室预约系统</div>
        </div>
        <div>
          <el-dropdown>
            <div style="display: flex; align-items: center; cursor: pointer">
              <img src="@/assets/imgs/logo.png" alt="" style="width: 20px; border-radius: 50%" />
              <div style="margin-left: 3px">管理员</div>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              <span>实验室管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              <span>用户管理</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main><router-view /></el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script setup>
import { Menu as IconMenu, House, User } from '@element-plus/icons-vue'
import { el } from 'element-plus/es/locales.mjs'
import router from '@/router'

const logout = () => {
  // 退出登录逻辑
  router.push('/login')
}
</script>
