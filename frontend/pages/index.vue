<template>
  <v-row align="center" justify="center">

    <v-col class="my-auto">
      <v-card
        class="mx-auto"
        color="grey darken-3"
        max-width="600"
        :loading="isUpdating"
      >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>

        <v-card-title>
          <v-row align="start">
            <v-col>
              <div class="text-caption grey--text text-uppercase">
                Temperature
              </div>
              <div class="white--text">
                <span
                  class="text-h3 font-weight-black"
                  v-text="temperature || '—'"
                ></span>
                <strong v-if="temperature">ºC</strong>
              </div>
            </v-col>

            <v-col>
              <div class="text-caption grey--text text-uppercase">
                Humidity
              </div>
              <div class="white--text">
                <span
                  class="text-h3 font-weight-black"
                  v-text="humidity || '—'"
                ></span>
                <strong v-if="humidity">%</strong>
              </div>
            </v-col>

          </v-row>

          <v-spacer></v-spacer>
          <v-tooltip top>
            <template #activator="{ on, attrs }">
              <v-btn
                alt="Atualizar"
                icon
                class="align-self-start"
                size="28"
                :disabled="isUpdating"
                v-bind="attrs"
                v-on="on"
                @click="loadData()"
              >
                <v-icon color="grey lighten-1">mdi-refresh</v-icon>
              </v-btn>
            </template>
            <span>Force update</span>
          </v-tooltip>

        </v-card-title>

        <v-card-text class="pt-0">
          <v-row>
            <v-col>
              <v-checkbox
                v-model="useHistory"
                dark
                label="Activate history"
              ></v-checkbox>
            </v-col>
            <v-col>
              <v-checkbox
                v-model="useAutomaticUpdate"
                dark
                label="Automatic update"
              ></v-checkbox>
            </v-col>
            <v-col>
              <v-text-field
                v-model="interval"
                :disabled="isUpdating"
                type="number"
                dark
                label="Automatic update (seconds)"
              ></v-text-field>
            </v-col>

          </v-row>

          <v-data-table
            v-if="useHistory"
            :headers="[
              {
                text: 'Hora',
                value: 'datetime'
              },
              {
                text: 'Temperatura',
                value: 'temperature'
              }, 
              {
                text: 'Umidade',
                value: 'humidity'
              }              
            ]"
            :items="history"
            :items-per-page="5"
            sort-by="datetime"
            :sort-desc="true"
            dark
          ></v-data-table>

          <v-divider class="my-2"></v-divider>
          <v-icon
            class="mr-2 grey--text"
            small
          >
            mdi-clock
          </v-icon>
          <span class="text-caption grey--text font-weight-light">Last updated at: {{ lastCheck }}</span>
        </v-card-text>
      </v-card>

    </v-col>
  </v-row>

</template>

<script src="./script.js" lang="ts"/>
<style href="./style.scss" />