Vagrant.require_version ">= 1.6.0"
ENV["VAGRANT_DEFAULT_PROVIDER"] = "docker"

# create and configure the docker container(s)
Vagrant.configure("2") do |config|
  config.vm.define "default" do |container|
    # disable synced folders
    container.vm.synced_folder ".", "/vagrant", disabled: true

    # configure the docker provider for vagrant
    container.vm.provider "docker" do |docker, override|
      # stick with has_ssh = false as with has_ssh = true
      # it is sometimes flaky:
      # https://github.com/mitchellh/vagrant/issues/5027
      docker.has_ssh = false
      docker.remains_running = true

      # specify the docker image to use
      docker.image = "benjixx/vagrant-centos6"

      docker.volumes = [
        "/sys/fs/cgroup:/sys/fs/cgroup:ro"  # cgroup read-only access required for systemd
      ]

      docker.privileged = true
    end
  end
end
